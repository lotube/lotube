from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'username', 'email', 'last_login')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('id', 'username', 'email', 'password',
                           'date_joined', 'last_login', 'ip_address')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2',
                           'ip_address')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    readonly_fields = ('id', 'date_joined', 'last_login',)

    search_fields = ('id', 'username', 'email',)
    ordering = ('id',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
