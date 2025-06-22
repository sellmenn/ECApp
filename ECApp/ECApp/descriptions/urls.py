from django.urls import path
from .views import DescriptionView

urlpatterns = [
    path('', DescriptionView.as_view(), name='descriptions'),
]
