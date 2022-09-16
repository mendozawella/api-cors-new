from dataclasses import fields
from rest_framework import serializers
from .models import Itasset

class ItassetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itasset
        fields = ['id', 'itemnumber', 'assetname', 'description', 'price', 'quantity', 'borrowersname']
