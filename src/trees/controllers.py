import binascii,os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from services.utils import paginator
from trees.models import PlantedTree, Tree
from trees.serializers import (
    TreeCreateSerializer,
    TreeRetriveSerializer,
    PlatendTreeRetriveSerializer,
    PlatendTreeCreateSerializer
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
    
    @classmethod
    def list_planted_trees(cls,request,id_tree):
        planted_trees_objs = cls.modes_planted_tree.objects.filter(tree_id=id_tree).order_by('id')
        return paginator(planted_trees_objs, "planted_trees", PlatendTreeRetriveSerializer, **request)
    
    @classmethod
    def plant_tree(cls,request):
        serializer_tree = PlatendTreeCreateSerializer(data=request)
        if serializer_tree.is_valid(raise_exception=True):
            planted_tree_info = serializer_tree.data
            planted_tree_info['longitude'],planted_tree_info['latitude'] = planted_tree_info['location']
            del planted_tree_info['location']

            planted_tree_obj = cls.modes_planted_tree.objects.create(**planted_tree_info)
            return planted_tree_obj
        else:
            return {
                "data":{"message": "an error has occured"}
            }
    