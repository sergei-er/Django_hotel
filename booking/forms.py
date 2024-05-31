from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out', 'additional_services']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        # Проверка на дату заезда и дату выезда
        if check_in and check_in < timezone.now().date():
            raise forms.ValidationError("Дата бронирования не может быть прошедшим числом")
        if check_out and check_out < timezone.now().date():
            raise forms.ValidationError("Дата бронирования не может быть прошедшим числом")
        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError("Дата выезда > дата заезда")

        # Проверка доступности номера
        if room and check_in and check_out:
            temp_booking = Booking(room=room, check_in=check_in, check_out=check_out)
            if not temp_booking.is_room_available():
                raise forms.ValidationError("Бронирование нефозможно, выберите другой номер или другие даты бронирования")
        
        return cleaned_data