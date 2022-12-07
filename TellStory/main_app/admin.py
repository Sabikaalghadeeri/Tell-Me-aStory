from django.contrib import admin

# Register your models here.
from .models import OwnStory, StoryTitle
# Register your models here.

admin.site.register(OwnStory)
admin.site.register(StoryTitle)