from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import VeihcleForm

def index(request):
    form = VeihcleForm()
    if request.method == 'POST':
        form = VeihcleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    context = {'form': form}
    return render(request, 'add_vehicle/index.html', context)
