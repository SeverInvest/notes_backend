from django.contrib import admin

# Register your models here.
from apps.users.models import User
from django.contrib.auth import admin as auth_admin


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    pass