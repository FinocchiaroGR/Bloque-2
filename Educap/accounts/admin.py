from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'is_staff', 'last_login')
    list_filter = ('is_active', 'is_staff', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups',)


admin.site.register(UserModel, UserAdmin)
admin.site.register(MiembroStaff)
admin.site.register(Estudiante)
