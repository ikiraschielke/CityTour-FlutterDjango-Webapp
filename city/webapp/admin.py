from django.contrib import admin
from .models import Landmark, Media, TextBlock

# Register your models here for the Django Admin Page
# http://127.0.0.1:8000/admin/login/?next=/admin/
# user: Superuser
# pw: superpassword

admin.site.register(Landmark)
admin.site.register(Media)
admin.site.register(TextBlock)