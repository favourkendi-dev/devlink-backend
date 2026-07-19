from django.urls import path
from .views import RegisterView

# URL patterns specific to the accounts app this gets included into the main project urls.py next

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]