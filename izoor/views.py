from uuid import UUID

from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from izoor.models import Goods
from izoor.serializers import GoodSerializator


# class GoodsApiView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

# стандартный метод вывода
class GoodsApiView(APIView):
    def get(self, request):
        goods = Goods.objects.all().values()
        goods_serialized = GoodSerializator(goods, many=True).data
        return Response({'posts': goods_serialized})

    def post(self, request):
        serializer = GoodSerializator(data=request.data)
        serializer.is_valid(raise_exception=True)
        # new_good = Goods.objects.create(
        #     barcode=request.data['barcode'],
        #     name=request.data['name'],
        #     price=request.data['price'],
        #     supplier_id=[UUID('supplier_id')],
        #     category_id=[UUID('category_id')],
        # )

        return Response({'post': 'GoodSerializator(new_good).data'})
