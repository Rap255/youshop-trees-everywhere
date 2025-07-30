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
from accounts.controllers import AccountsControllers


class UsersControllers():
    
    model = UserModel
    model_profile = Profile

    @classmethod
    def create_user(cls,request):
        serializer_user = UserCreateSerializer(data=request)
        if serializer_user.is_valid(raise_exception=True):
            serializer_user_dict = serializer_user.data
            serializer_user_dict["type_of_access_id"] = int(serializer_user_dict["type_of_access"])
            del serializer_user_dict["type_of_access"]

            user_obj = cls.model.objects.create(**serializer_user_dict)
            user_obj.set_password(request["password"])
            user_obj.save()

            if serializer_user_dict["type_of_access_id"] == 2:
                profile_obj = cls.model_profile.objects.create(user_id=user_obj.id)
                accont_user_obj = AccountsControllers.create_account_user(id_user=user_obj.id,id_account=int(request["accounts"]))
            return user_obj
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
        users_objs = cls.model.objects.all().order_by('id')
        return paginator(users_objs, "users", UserRetriveSerializer, **request)
    