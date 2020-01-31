from django.contrib import admin
from mainapp.models import CarMaker


@admin.register(CarMaker)
class CarAdmin(admin.ModelAdmin):
    search_fields = 'name',
