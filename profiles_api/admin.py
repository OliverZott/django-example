from django.contrib import admin
from profiles_api import models

# Shown in http://127.0.0.1:8000/admin/profiles_api/
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
