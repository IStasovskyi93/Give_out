from django.contrib import admin
from .models import *

admin.site.register(Category)
# admin.site.register(Institution)


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


admin.site.register(Donation)

