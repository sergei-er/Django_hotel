from django.urls import path, include

from booking import views

app_name = "booking"

urlpatterns = [
    path('', views.booking, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('additional_services/', views.additional_services, name='additional_services'),
]
