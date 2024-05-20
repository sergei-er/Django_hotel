from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hotel_numbers(request):
    return render(request, 'hotel_numbers.html')