from django.contrib import admin

from TourApp.models import bookings,category,hotels,status,users,tourguide,destinations
# Register your models here.

admin.site.register(bookings )
admin.site.register( category)
admin.site.register( hotels)
admin.site.register( status)
admin.site.register( users)
admin.site.register( tourguide)
admin.site.register(destinations)