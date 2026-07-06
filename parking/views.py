
from django.shortcuts import render, redirect
from .models import Parking
from .forms import ParkingForm
#parking project
def home(request):
    data = Parking.objects.all()
    return render(request, 'home.html', {'data': data})


def add(request):
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParkingForm()

    return render(request, 'form.html', {'form': form})


def edit(request, id):
    record = Parking.objects.get(id=id)

    if request.method == 'POST':
        form = ParkingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParkingForm(instance=record)

    return render(request, 'form.html', {'form': form})


def delete(request, id):
    record = Parking.objects.get(id=id)
    record.delete()
    return redirect('/')
from rest_framework import viewsets
from .serializers import ParkingSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer