# ECApp

This is a simple Django web application for early childhood educators to upload photos of classroom activities and receive automated descriptions using the OpenAI API. The project is ready for deployment on Heroku.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```
3. Run migrations and start the development server:
   ```bash
   python ECApp/manage.py migrate
   python ECApp/manage.py runserver
   ```

## Deployment

Create a Heroku app and push this repository. Heroku will detect the `Procfile` and use `gunicorn` to serve the application. Ensure the `OPENAI_API_KEY` config var is set in Heroku.
