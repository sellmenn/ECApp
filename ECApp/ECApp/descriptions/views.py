from django.shortcuts import render
from django.views import View
from django.conf import settings
import openai
import base64

class DescriptionView(View):
    template_name = "descriptions/upload.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        image = request.FILES.get("photo")
        context = {}
        if image:
            openai.api_key = settings.OPENAI_API_KEY
            image_data = base64.b64encode(image.read()).decode("utf-8")
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4-vision-preview",
                    messages=[{
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe the preschool activities happening in this photo."},
                            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_data}"}
                        ]
                    }]
                )
                description = response.choices[0].message.content.strip()
                context["description"] = description
            except Exception as e:
                context["error"] = str(e)
        return render(request, self.template_name, context)

