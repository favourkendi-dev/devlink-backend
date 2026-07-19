from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


# Handles POST requests to create a new user without writing the logic ourselves  it uses our serializer to do the work.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer