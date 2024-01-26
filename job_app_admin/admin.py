from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # admin table view
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_name',)  # it is a tuple / if '-first_name' - will order from z to a
    readonly_fields = ('first_name',)  # it is a tuple


admin.site.register(Form, FormAdmin)
