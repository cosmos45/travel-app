from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from cities.models import Cities
from cities.serializers import CitiesSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
