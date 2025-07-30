import datetime
import calendar
from django.db import models
from django.db.models import fields
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from services.utils import format_date
from trees.models import Tree, PlantedTree


class TreeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        fields = [
            "name",
            "scientific_name"
        ]


class TreeRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = "__all__"


class PlatendTreeCreateSerializer(serializers.Serializer):
    
    user_id = serializers.CharField(max_length=5)
    tree_id = serializers.CharField(max_length=5)
    account_id = serializers.CharField(max_length=5)
    age = serializers.IntegerField()
    planted_at = serializers.DateTimeField()
    longitude = serializers.DecimalField(max_digits=9,decimal_places=6)
    latitude = serializers.DecimalField(max_digits=9,decimal_places=6)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = (data['longitude'],data['latitude'])
        del data['longitude']
        del data['latitude']
        return data


class PlatendTreeRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantedTree
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['planted_at'] = format_date(data['planted_at'])
        data['tree'] = TreeCreateSerializer(Tree.objects.get(id=data['tree'])).data
        return data