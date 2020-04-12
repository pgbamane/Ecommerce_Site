from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from users_app.forms import CustomUserCreationForm, CustomUserChangeForm


# admin.site.register(get_user_model())

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()

    list_display = ('first_name', 'last_name', 'email_id', 'phone_number', 'is_active')
    list_filter = ('first_name', 'last_name', 'email_id', 'phone_number', 'is_active')

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email_id', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email_id', 'password1', 'password2', 'phone_number', 'is_active')
        })
    )
    search_fields = ('email_id',)
    ordering = ('email_id',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(get_user_model(), UserAdmin)
