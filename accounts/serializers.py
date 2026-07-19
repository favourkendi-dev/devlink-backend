from django.contrib.auth.models import User
from rest_framework import serializers


# Handles turning incoming registration data into a real User and validates it before saving

class RegisterSerializer(serializers.ModelSerializer):

    # We add password separately so we can mark it write_only
   
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    # This runs when we call serializer.save() in the view We override it because passwords need to be hashed  not stored as plain text
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user