from django.contrib import admin
from .models import Machines

# Register your models here.
@admin.register(Machines)
class MachinesAdmin(admin.ModelAdmin):
    list_display = ('machine_type', 'specification', 'status')
    list_filter = ('machine_type',)
