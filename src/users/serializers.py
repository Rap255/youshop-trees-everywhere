import datetime
import calendar
from django.db import models
from django.db.models import fields
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from users.models import UserModel,Profile
from services.utils import format_date


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = [
            "email",
            "type_of_access_id",
            "password",
            "first_name",
            "last_name",
        ]


class UserRetriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = [
            "id",
            "type_of_access",
            "email",
            "first_name",
            "last_name",
            "is_active"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        profile_info = Profile.objects.get(id=data["id"])
        data["profile"] = {
            "about": profile_info.about,
            "joined": format_date(str(profile_info.joined))
        }
        data["type_of_access"] = "Admin" if data["type_of_access"] == 1 else "Standard"
        return data
