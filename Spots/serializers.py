from rest_framework import serializers

from Spots.models import Spots


class SpotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spots
        fields = 'state', 'image', 'description', 'city', 'spot_name', 'cost'
