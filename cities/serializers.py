from rest_framework import serializers

from cities.models import Cities


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = 'state', 'image', 'description', 'city'
