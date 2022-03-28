from email import contentmanager
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner, VehicleDetail



def index(request):
    vehicles = VehicleDetail.objects.all()
    context = {'vehcile_details':vehicles}
    return render(request, 'home/index.html', context)