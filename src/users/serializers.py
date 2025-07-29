import datetime
import calendar
from django.db import models
from django.db.models import fields
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from users.models import UserModel
from services.utils import format_date


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = [
            "email",
            "type_of_access_id",
            "password",
            "first_name"
        ]


class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
