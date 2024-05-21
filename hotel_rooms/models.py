from django.db import models

# Create your models here.
class HotelRoom(models.Model):
    ROOM_TYPES = [
        ('standard', 'Standard'),
        ('lux', 'Lux'),
        ('family', 'Family'),
    ]

    room_number = models.IntegerField(unique=True, verbose_name='Номер')
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name='Тип комнаты')
    room_capacity = models.IntegerField(verbose_name='Количество мест')
    photo = models.ImageField(upload_to='room_photos/', verbose_name='Фото')
    room_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за ночь')

    class Meta:
        db_table = 'hotel_rooms'
        verbose_name = 'Гостиничныt номера'
        verbose_name_plural = 'Гостиничныt номера'

    def __str__(self):
        return f"Room {self.room_number} - {self.get_room_type_display()}"