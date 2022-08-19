from uuid import UUID

from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from izoor.models import Goods, Organization, POSUser
from izoor.serializers import GoodSerializator, OrganizationSerializator, POSUserSerializator


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

class OrganizationApiView(APIView):
    def get(self, request):
        organizations = Organization.objects.all().values()
        org_serialized = OrganizationSerializator(organizations, many=True).data
        return Response({'posts': org_serialized})

    def post(self, request):
        serializer = OrganizationSerializator(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put is not allowed"})
        try:
            intance = Organization.objects.get(pk=pk)
        except:
            return Response({"error": "Object is not exist"})

        serializer = OrganizationSerializator(data=request.data, instance=intance)
        serializer.is_valid()
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Delete is not allowed"})
        try:
            instance = Organization.objects.get(pk=pk)
        except:
            return Response({"error": "Object is not exist"})
        instance.delete()
        return Response({'post': 'deleted'})


class POSUserApiView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            users = POSUser.objects.all().values()
            users_serialized = POSUserSerializator(users, many=True).data
            return Response({'posts': users_serialized})
        user = POSUser.objects.get(pk=pk)
        user_serialized = POSUserSerializator(user).data
        return Response({'posts': user_serialized})


class POSUserAPIList(generics.ListCreateAPIView):
    queryset = POSUser.objects.all()
    serializer_class = POSUserSerializator


class POSUserAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = POSUser.objects.all()
    serializer_class = POSUserSerializator




    # def post(self, request):
    #     serializer = OrganizationSerializator(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method Put is not allowed"})
    #     try:
    #         intance = Organization.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object is not exist"})
    #
    #     serializer = OrganizationSerializator(data=request.data, instance=intance)
    #     serializer.is_valid()
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method Delete is not allowed"})
    #     try:
    #         instance = Organization.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object is not exist"})
    #     instance.delete()
    #     return Response({'post': 'deleted'})
