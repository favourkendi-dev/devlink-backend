from django.urls import path
from .views import RegisterView, ProtectedTestView, ProfileDetailView
# A list of URL patterns that Django will use to route incoming requests to the appropriate view
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', ProtectedTestView.as_view(), name='protected'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]