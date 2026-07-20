from django.contrib import admin
from .models import Post

# Registering Post so it shows up in the Django admin panel letting us view or add or edit posts through the browser
admin.site.register(Post)
