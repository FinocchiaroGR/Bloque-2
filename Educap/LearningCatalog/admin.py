from django.contrib import admin
from .models import *
import string
# Register your models here.


class AlphabetFilter(admin.SimpleListFilter):
    title = 'alfabeto'
    parameter_name = 'alfabeto'

    def lookups(self, request, model_admin):
        abc = list(string.ascii_lowercase)
        return ((c.upper(), c.upper()) for c in abc)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(nombre__startswith=self.value())


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'descripción', 'fechaCreada')
    list_filter = (AlphabetFilter, 'fechaCreada')
    ordering = ('nombre',)


class ArchivoAdminInline(admin.TabularInline):
    model = Archivo


class VideoAdminInline(admin.TabularInline):
    model = (Video)


class LeccionAdmin(admin.ModelAdmin):
    inlines = (ArchivoAdminInline, VideoAdminInline)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Leccion, LeccionAdmin)
