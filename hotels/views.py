from django.shortcuts import render
from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer


class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


