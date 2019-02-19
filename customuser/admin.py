from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from customuser.models import CustomUser
from django.contrib.auth.models import Group
from hijack_admin.admin import HijackUserAdminMixin

class CustomUserAdmin(UserAdmin, HijackUserAdminMixin):
	pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)