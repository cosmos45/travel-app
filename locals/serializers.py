from rest_framework import serializers

from locals.models import Locals


class LocalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locals
        fields = 'state', 'image', 'description', 'city', 'locality', 'also_find'
