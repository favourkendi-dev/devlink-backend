from django.db import models
from django.contrib.auth.models import User


# A single post that will be created by a developer 
class Post(models.Model):

    # Who wrote this post If the User is deleted delete their posts too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # The actual text content of the post
    content = models.TextField()

    # Automatically set to the current time when the post is FIRST created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updated to the current time every time the post is saved or edited
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Show newest posts first by default like a real feed
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
