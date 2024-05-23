from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AdditionalService, Booking
from .forms import BookingForm

from django.contrib.auth.decorators import login_required


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Устанавливаем текущего пользователя в поле user формы
            booking.user = request.user

            # Вычисляем стоимость
            room = booking.room
            days = (booking.check_out - booking.check_in).days
            room_total_price = days * room.room_price 

            # Вычисляем стоимость дополнительных услуг
            additional_services = form.cleaned_data['additional_services']
            additional_services_total_price = sum(service.service_price for service in additional_services)

            # Общая стоимость
            total_price = room_total_price + additional_services_total_price

            # Сохраняем бронирование
            booking.total_price = total_price
            booking.save()
            form.save_m2m()  # сохраняем многие-ко-многим поля

            # Получаем последнюю запись в таблице Booking
            latest_booking = Booking.objects.latest('id')

            
            # Передаем общую стоимость в контекст
            return render(request, 'booking_success.html', {'total_price': latest_booking.total_price})

    else:
        form = BookingForm()
    context = {
        'form': form,
    }
    return render(request, 'booking.html', context)


def booking_success(request):
    return render(request, 'booking_success.html')

def additional_services(request):
    services = AdditionalService.objects.all()
    return render(request, 'additional_services.html', {'services': services})
