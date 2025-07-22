from django.shortcuts import render
from django.views import generic
from django.templatetags.static import static
from .models import Machines


# Create your views here.
class MachineList(generic.ListView):
    queryset = Machines.objects.all().filter(status=1).order_by("machine_type")
    template_name = "machines_list.html"
    paginate_by = 6
    context_object_name = "machines"
