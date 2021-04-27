from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from locals.models import Locals
from locals.serializers import LocalsSerializer


class LocalsViewSet(viewsets.ModelViewSet):
    queryset = Locals.objects.all()
    serializer_class = LocalsSerializer
