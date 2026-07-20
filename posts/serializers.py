from rest_framework import serializers
from .models import Post


# Handles turning a Post into JSON for the frontend to display and validating incoming JSON data when creating or editing a post
class PostSerializer(serializers.ModelSerializer):

    # we set that automatically based on who's logged in see the view
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
