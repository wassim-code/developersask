from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_admin']
    list_filter = ('is_admin',)
    fieldsets = [
        [None, {'fields': ('password', 'email', 'username')}],
        ['Permissions', {'fields': ('is_active', 'is_staff', 'is_admin')}],
    ]
    add_fieldsets = [
        [None, {'fields': ('email', 'username', 'password1', 'password2')}],
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)