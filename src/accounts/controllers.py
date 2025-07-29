import binascii,os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from accounts.models import Account
from services.utils import paginator
from accounts.serializers import(
    AccountCreateSerializer,
    AccountRetriveSerializer,
    AccountsRetriveSerializer
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
    
    @classmethod
    def list_accounts(cls,request):
        account_objs = cls.model.objects.all().order_by('id')
        return paginator(account_objs, "accounts", AccountsRetriveSerializer, **request)
    
    @classmethod
    def deactivate_activate_account(cls,id_account):
        account_obj = cls.model.objects.get(id=id_account)
        account_obj.active = not(account_obj.active)
        account_obj.save()
        return True