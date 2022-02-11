from inspect import formatannotationrelativeto
from django.shortcuts import render
from rest_framework import generics
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TourApp.models import bookings,category,hotels,status,users,tourguide,destinations
from TourApp.serializers import  bookingsSerializer,categorySerializer,hotelsSerializer,statusSerializer,usersSerializer,tourguideSerializer,destinationsSerializer

# Create your views here.

# @csrf_exempt
# def adminAPI (request,id=0):
#     if request.method == 'GET':
#         user = users.objects.all()
#         admins_serializer = usersSerializer(user,many= True)
#         return JsonResponse(admins_serializer.data,safe=False)
#     elif request.method == 'POST':
#         admins_data= JSONParser().parse(request)
#         admins_serializer = usersSerializer(data=admins_data)
#         if admins_serializer.is_valid():
#             admins_serializer.save()
#             return JsonResponse("Added Succesfully",safe=False)
#         return JsonResponse("Fail To add record",safe=False)
#     elif request.method== 'PUT':
#         admins_data= JSONParser().parse(request)
#         adminstrator = users.objects.get(userId=admins_data['userId'])
#         admins_serializer = usersSerializer(adminstrator,data=admins_data)
#         if admins_serializer.is_valid():
#             admins_serializer.save()
#             return JsonResponse("Updated Succesfully",safe=False) 
#         return JsonResponse("Fail To update record",safe=False)
#     elif request.method== 'DELETE':
#         adminstrator = usersSerializer.objects.get(userId=id)
#         users.delete()
#         return JsonResponse("Updated Succesfully",safe=False) 
        

class ListUsers(generics.ListCreateAPIView):
    queryset= users.objects.all()
    serializer_class = usersSerializer

class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset= users.objects.all()
    serializer_class = usersSerializer


class ListDestination(generics.ListCreateAPIView):
    queryset = destinations.objects.all()
    serializer_class = destinationsSerializer
class DetailDestination(generics.RetrieveUpdateDestroyAPIView):
    queryset = destinations.objects.all()
    serializer_class= destinationsSerializer

class ListTourGuide(generics.ListCreateAPIView):
    queryset = tourguide.objects.all()
    serializer_class = tourguideSerializer
class DetailTourGuide(generics.RetrieveUpdateDestroyAPIView):
    queryset = tourguide.objects.all()
    serializer_class = tourguideSerializer

class ListHotel(generics.ListCreateAPIView):
    queryset = hotels.objects.all()
    serializer_class = hotelsSerializer
class DetailHotel(generics.RetrieveUpdateDestroyAPIView):
    queryset = hotels.objects.all()
    serializer_class= hotelsSerializer

class ListBookings(generics.ListCreateAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingsSerializer
class DetailBookings(generics.RetrieveUpdateDestroyAPIView):
    queryset = bookings.objects.all()
    serializer_class = bookingsSerializer

class ListCategory(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer

class ListStatus(generics.ListCreateAPIView):
    queryset = status.objects.all()
    serializer_class = statusSerializer
class DetailStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = status.objects.all()
    serializer_class = statusSerializer