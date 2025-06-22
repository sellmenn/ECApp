# ECApp

This is a simple Django web application for early childhood educators to upload photos of classroom activities and receive automated descriptions using the OpenAI API. The project is ready for deployment on Heroku.

Users must log in before accessing the evaluation form. Create a superuser with:
```bash
python ECApp/manage.py createsuperuser
```
Then sign in at `/login/`.

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

Create a Heroku app and push this repository. Heroku will detect the `Procfile` and use `gunicorn` to serve the application. Set the `OPENAI_API_KEY` and `ALLOWED_HOSTS` config vars in Heroku so the app can authenticate and serve requests.
