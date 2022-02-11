from django.conf.urls import *
from TourApp.views import *
from django.contrib import admin
from TourApp.models import bookings,category,hotels,status,users,tourguide,destinations


urlpatterns = [
    url(r'^users$',ListUsers.as_view(),name='users'),
    url(r'^users/<int:pk>$',DetailUsers.as_view() ,name = 'singleuser'),

    url(r'^Destinations$',ListDestination.as_view(), name='destination'),
    url(r'^Destinations/([0-9]+)$',DetailDestination.as_view(), name='singledestination'),

    url(r'^hotels$',ListHotel.as_view(), name='hotel'),
    url(r'^hotels/([0-9]+)$',DetailHotel.as_view(), name='singlehotel'),

    url(r'^bookings$',ListBookings.as_view(), name='bookings'),
    url(r'^bookings/([0-9]+)$',DetailBookings.as_view(), name='singlebooking'),

    url(r'^categories$',ListCategory.as_view(), name='category'),
    url(r'^categories/([0-9]+)$',DetailCategory.as_view(), name='singlecategory'),

    url(r'^status$',ListStatus.as_view(), name='status'),
    url(r'^status/([0-9]+)$',DetailStatus.as_view(), name='singlestatus'),
]

