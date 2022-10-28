from rest_framework import serializers
from .models import prods, coordsprods


class prodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = prods
        fields = ["ref", "zipcode", "store", "amount"]


class coordsprodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = coordsprods
        fields = ["lat", "long", "ref"]
