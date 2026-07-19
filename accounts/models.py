from django.db import models
from django.contrib.auth.models import User

# stores extra developer info that Django's built-in User model doesn't have, like bio, github_url and skills

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    skills = models.CharField(max_length=255, blank=True)


    #Controls how a Profile shows up as text
    def __str__(self):
        return self.user.username