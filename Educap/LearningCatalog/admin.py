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
            return queryset.filter(Nombre__startswith=self.value())

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Descripción','FechaCreada')
    list_filter = (AlphabetFilter, 'FechaCreada')
    ordering =('Nombre',)

admin.site.register(Categoria, CategoriaAdmin)
