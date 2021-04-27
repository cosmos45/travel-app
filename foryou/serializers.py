from rest_framework import serializers

from foryou.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = 'state', 'no_of_cities', 'image', 'no_of_days', 'total_expense', 'destinations', 'day_overview', 'single_occupancy', 'twin_sharing', 'triple_sharing', 'infant', 'child_with_mat', 'child_without_mat', 'child'
