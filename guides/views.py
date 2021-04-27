from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from guides.models import Guides
from guides.serializers import GuideSerializer


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guides.objects.all()
    serializer_class = GuideSerializer
