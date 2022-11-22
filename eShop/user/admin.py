from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import UserAcc, UserAccProfile


class UserAccAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
        (_('Important Dates'), {'fields': ('last_login', )}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email',
                'name',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_superuser',
            )
        }),
    )


admin.site.register(UserAcc, UserAccAdmin)
admin.site.register(UserAccProfile)
