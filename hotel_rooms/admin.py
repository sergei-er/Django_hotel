from django.contrib import admin

# Register your models here.

from .models import HotelRoom

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'room_capacity', 'room_price')
    list_filter = ('room_type',)
    search_fields = ('room_number',)