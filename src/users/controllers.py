import binascii,os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from users.models import UserModel,Profile
from services.utils import paginator
from users.serializers import(
    UserCreateSerializer,
    UserRetriveSerializer
)


class UsersControllers():
    
    model = UserModel
    model_profile = Profile

    @classmethod
    def create_user(cls,request):
        serializer_account = UserCreateSerializer(data=request)
        if serializer_account.is_valid(raise_exception=True):
            account_obj = cls.model.objects.create(**serializer_account.data)
            return account_obj
        else:
            return {
                "data":{"message": "an error has occured"}
            }

    @classmethod
    def list_user(cls,id_user):
        user_obj = cls.model.objects.get(id=id_user)
        return UserRetriveSerializer(user_obj).data
    
    @classmethod
    def list_users(cls,request):
        account_objs = cls.model.objects.all().order_by('id')
        return paginator(account_objs, "users", UserRetriveSerializer, **request)
    