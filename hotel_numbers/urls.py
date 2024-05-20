from django.urls import path, include

from hotel_numbers import views

app_name = 'hotel_numbers'

urlpatterns = [
    path('', views.hotel_numbers, name='hotel_numbers'),
]