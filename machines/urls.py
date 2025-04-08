from django.urls import path
from . import views


urlpatterns = [
    path("machines/", views.MachineList.as_view(), name="machines"),
]
