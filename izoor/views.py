from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from izoor.models import Goods
from izoor.serializers import GoodsSerializer


class GoodsApiView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
