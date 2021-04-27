from rest_framework import serializers

from food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = 'state', 'image', 'description', 'city', 'cost_for_2', 'restaurant', 'must try'
