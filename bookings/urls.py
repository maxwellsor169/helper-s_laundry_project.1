from django.urls import path
from .views import book_appointment, list_appointments, edit_appointment


urlpatterns = [
     path('book_appointment/', book_appointment, name='book_appointment'),
     path('list_appointments/', list_appointments, name='list_appointments'),
     path('edit-appointment/<int:booking_id>/', edit_appointment, name='edit_appointment'),
]