from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import HotelRoom


def hotel_rooms(request):
    rooms = HotelRoom.objects.all()
    return render(request, 'numbers.html', {'rooms': rooms})