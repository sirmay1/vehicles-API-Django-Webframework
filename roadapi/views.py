from django.shortcuts import render
from .serializers import TravelSerializer
from .models import Travel
from rest_framework import viewsets

class TravelView(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer






