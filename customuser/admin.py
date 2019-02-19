from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
	pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)