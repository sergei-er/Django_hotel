from django.contrib import admin
from booking.models import Booking, AdditionalService

class AdditionalServiceInline(admin.TabularInline):
    model = Booking.additional_services.through
    extra = 1

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'total_price', 'get_additional_services')
    list_filter = ('room', 'check_in', 'check_out')
    search_fields = ('user__username', 'room__room_number')
    inlines = [AdditionalServiceInline]

    def get_additional_services(self, obj):
        return ", ".join([service.name for service in obj.additional_services.all()])
    get_additional_services.short_description = 'Additional Services'



@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)