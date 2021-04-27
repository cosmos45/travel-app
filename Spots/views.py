from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from Spots.models import Spots
from Spots.serializers import SpotsSerializer


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Spots.objects.all()
    serializer_class = SpotsSerializer
