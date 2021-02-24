

# Register your models here.
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass