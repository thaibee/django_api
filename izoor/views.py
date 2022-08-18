from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from izoor.models import Goods
from izoor.serializers import GoodsSerializer


# class GoodsApiView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

class GoodsApiView(APIView):
    def get(self, request):
        return Response({'name': 'Любаня'})
