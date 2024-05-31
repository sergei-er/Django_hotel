from django.db import models

from hotel_rooms.models import HotelRoom
from users.models import User

class AdditionalService(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'additional_service'
        verbose_name = 'Доп. услуги'
        verbose_name_plural = 'Доп. услуги'

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    additional_services = models.ManyToManyField(AdditionalService, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'booking'
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

    def __str__(self):
        return f"Booking for {self.room} from {self.check_in} to {self.check_out}"
    
    def is_room_available(self):
        overlapping_bookings = Booking.objects.filter(
            room=self.room,
            check_out__gt=self.check_in,
            check_in__lt=self.check_out
        ).exclude(pk=self.pk)
        return not overlapping_bookings.exists()