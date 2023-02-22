from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
  fieldsets = (
    ("Personal info"), {"fields": ("email","password", "username", "profileIntroduce", "followerNum", "profileImg")}
    ),
  
  list_display=(
    "username",
    "profileIntroduce",
    "followerNum"
  )