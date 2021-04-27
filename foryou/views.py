from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from foryou.models import State
from foryou.serializers import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer