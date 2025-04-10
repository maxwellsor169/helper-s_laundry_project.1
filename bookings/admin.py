from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from datetime import time
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'user', 'machine_selected', 'appointment_date',
                    'appointment_time')
    search_fields = ['name']
    list_filter = ('appointment_date',)
    summernote_fields = ('requests')
