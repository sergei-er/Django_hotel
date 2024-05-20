from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hotel_rooms(request):
    return render(request, 'numbers.html')