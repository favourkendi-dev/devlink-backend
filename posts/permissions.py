from rest_framework import permissions


# Custom permission to allow anyone logged in to VIEW a post but only the post's original author can edit or delete it
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # These are read-only actions 
        if request.method in permissions.SAFE_METHODS:
            return True


        # if the person making the request is the post's author
        return obj.author == request.user