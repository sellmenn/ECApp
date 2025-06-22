from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

load_dotenv(".env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

evaluation_prompt = """
You are a pre-school teacher writing activity evaluations based on observations and photos of children.

Given the user's written observation and photo(s) of a child’s activity, write an evaluation containing:

1. **Observation summary** – Summarize the activity.
2. **Social-emotional development** – Describe any social or emotional growth observed.
3. **Physical development** – Mention gross or fine motor skills used.
4. **Natural environment awareness** – If relevant, describe any interaction with the surroundings.

Your evaluation must be objective, grounded only in the provided inputs. Do not speculate or describe the child’s appearance or clothing.
"""

class EvaluationView(LoginRequiredMixin, View):
    template_name = "descriptions/evaluate.html"
    login_url = "login"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        observation = request.POST.get("observation", "").strip()
        images = request.FILES.getlist("photo")
        context = {"observation": observation}

        if not observation and not images:
            context["error"] = "Please enter an observation or upload at least one photo."
            return render(request, self.template_name, context)

        # Start with system prompt and observation
        messages = [{"role": "system", "content": evaluation_prompt}]

        if observation:
            messages.append({"role": "user", "content": [{"type": "text", "text": f"Observation: {observation}"}]})
        else:
            messages.append({"role": "user", "content": [{"type": "text", "text": "No observation text provided."}]})

        # Add image content if available
        if images:
            image_parts = []
            for image in images:
                image_data = base64.b64encode(image.read()).decode("utf-8")
                mime_type = image.content_type
                image_parts.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{image_data}"
                    }
                })
            messages[-1]["content"].extend(image_parts)

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            evaluation = response.choices[0].message.content.strip()
            context["evaluation"] = evaluation

        except Exception as e:
            context["error"] = f"Failed to generate evaluation: {str(e)}"

        return render(request, self.template_name, context)
