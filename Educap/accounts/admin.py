from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.site_header = "Educap Admin Panel"
admin.site.site_title = "Educap Admin Panel"
admin.site.index_title = "Bienvenido al panel administrativo de Educap"


class UserAdmin(BaseUserAdmin):
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
