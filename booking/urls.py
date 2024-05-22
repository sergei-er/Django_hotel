from django.urls import path, include

from booking import views

app_name = "booking"

urlpatterns = [
    path('', views.booking, name='booking'),
]
