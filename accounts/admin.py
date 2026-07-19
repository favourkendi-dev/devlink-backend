from django.contrib import admin
from .models import Profile

# Registering Profile so it shows up in the Django admin panel this lets us view/add/edit Profile records through the browser.

admin.site.register(Profile)