from django.contrib import admin
from .models import Landmark, Media

# Register your models here.

admin.site.register(Landmark)
#admin.site.register(Media)

"""
#The admin interface has the ability to edit models on the same page as a parent model.
class MediaInline(admin.TabularInline):
    model = Media

class LandmarkAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]
"""