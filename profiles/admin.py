from django.contrib import admin

# Register your models here.

from .models import Profile,Record


admin.site.register(Profile)
admin.site.register(Record)