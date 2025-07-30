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