from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from food.models import Food
from food.serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
