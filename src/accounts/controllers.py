import binascii,os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from accounts.models import Account
from accounts.serializers import(
    AccountCreateSerializer,
    AccountRetriveSerializer
)

class AccountsControllers():
    
    model = Account

    @classmethod
    def create_account(cls,request):
        serializer_account = AccountCreateSerializer(data=request)
        if serializer_account.is_valid(raise_exception=True):
            account_obj = cls.model.objects.create(**serializer_account.data)
            return account_obj
        else:
            return {
                "data":{"message": "an error has occured"}
            }

    @classmethod
    def list_account(cls,account_id):
        account_obj = cls.model.objects.get(id=account_id)
        return AccountRetriveSerializer(account_obj).data