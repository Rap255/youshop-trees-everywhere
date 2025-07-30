import binascii,os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from services.utils import paginator
from trees.models import PlantedTree, Tree
from trees.serializers import (
    TreeCreateSerializer,
    TreeRetriveSerializer
)

class TreesControllers():

    model = Tree
    modes_planted_tree = PlantedTree

    @classmethod
    def create_tree(cls,request):
        serializer_tree = TreeCreateSerializer(data=request)
        if serializer_tree.is_valid(raise_exception=True):
            tree_obj = cls.model.objects.create(**serializer_tree.data)
            return tree_obj
        else:
            return {
                "data":{"message": "an error has occured"}
            }
        
    @classmethod
    def list_trees(cls,request):
        trees_objs = cls.model.objects.all().order_by('id')
        return paginator(trees_objs, "trees", TreeRetriveSerializer, **request)
    