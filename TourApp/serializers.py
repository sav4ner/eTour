
from inspect import formatannotationrelativeto
from django.db.models import fields
from rest_framework import serializers
from TourApp.models import bookings,category,hotels,status,users,tourguide,destinations

# class adminSerializer (serializers.ModelSerializer):
#     class Meta:
#         model= admin
#         fields (
#             'adminId',
#             'firstname ',
#             'lastname ',
#             'photo',
#             'email',
#             'contact ',
#             'username',
#         )

class usersSerializer (serializers.ModelSerializer):
    class Meta:
        model= users
        fields = (
            'userId',
            'firstname',
            'lastname',
            'nationality',
            'languages',
            'photo',
            'email',
            'contact',
            'username',
        )

class destinationsSerializer (serializers.ModelSerializer):
    class Meta:
        model= destinations
        fields = (
            'destinationId',
            'name',
            'description',
            'longitude',
            'latitude',
            'categori',
            'price',
            'imageurl',
            'url',
            'rating'
        )

class hotelsSerializer (serializers.ModelSerializer):
    class Meta:
        model= hotels
        fields = (
            'hotelId',
            'name',
            'description',
            'location',
            'city',
            'price',
            'imageurl',
            'url',
            'rating'
        )

class tourguideSerializer (serializers.ModelSerializer):
    class Meta:
        model= tourguide
        fields = (
            'userId',
            'firstname ',
            'lastname ',
            'languages',
            'photo',
            'email',
            'speciality',
            'contact',
            'status',
        )


class categorySerializer (serializers.ModelSerializer):
    class Meta:
        model= category
        fields = (
            'categories',
        )

class statusSerializer (serializers.ModelSerializer):
    class Meta:
        model= status
        fields = (
            'state',
        )


class bookingsSerializer (serializers.ModelSerializer):
    class Meta:
        model= bookings
        fields = (
            'bookingId',
            'firstname ',
            'lastname ',
            'email',
            'contact',
            'tourguide',
            'date',
            'Duration',
            'destination',
            'bill',
        )