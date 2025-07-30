import datetime
import calendar
from django.db import models
from django.db.models import fields
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from accounts.models import Account, AccountUser
from users.models import UserModel
from services.utils import format_date


class AccountCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "name"
        ]


class AccountRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = (
            "name"
        )

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data["account_name"] = Account.objects.get(id=data["account"]).name
            data["user_name"] = UserModel.objects.get(id=data["user"]).name
            return data


class AccountsRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def to_representation(self, instance):
            data = super().to_representation(instance)
            data["created"] = format_date(str(data["created"]))
            return data
    

class AccountsUserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = "__all__"

    def to_representation(self, instance):
            data = super().to_representation(instance)
            data["created"] = format_date(str(data["created"]))
            return data