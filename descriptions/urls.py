from django.urls import path
from .views import *

urlpatterns = [
    path('', EvaluationView.as_view(), name='descriptions'),
]
