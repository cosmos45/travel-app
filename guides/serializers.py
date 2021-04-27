from rest_framework import serializers

from guides.models import Guides


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guides
        fields = 'state', 'image', 'description', 'city'
