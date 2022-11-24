from django.contrib import admin
from .models import UserProfile
from django.contrib.auth import get_user_model


# Register your models here.
User = get_user_model()

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user', 'avatar']
    