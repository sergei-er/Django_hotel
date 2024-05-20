from django.urls import path, include

from hotel_rooms import views

app_name = 'hotel_rooms'

urlpatterns = [
    path('', views.hotel_rooms, name='numbers'),
]