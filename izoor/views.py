from uuid import UUID
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from izoor.models import Goods, Organization, POSUser, GoodsCategory, Women
from izoor.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from izoor.serializers import GoodSerializator, OrganizationSerializator, POSUserSerializator, WomenSerializator


class WomenCLView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializator
    permission_classes = [IsAuthenticated]


class WomanRUView(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializator
    permission_classes = [IsOwnerOrReadOnly]


class WomanRDView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializator
    #самодельный класс лежит в permissions.py
    permission_classes = (IsAdminOrReadOnly, )


class GoodAPIModelView(viewsets.ModelViewSet):
    # убрал quesryset добавь basename в url
    # queryset = Goods.objects.all()
    serializer_class = GoodSerializator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Goods.objects.all()[:5]
        return Goods.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = GoodsCategory.objects.all()
        return Response({'cats': [(c.name.strip(), c.slug) for c in cats]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = GoodsCategory.objects.get(pk=pk)
        return Response({'cats': cat.name.strip()})


class OrganizationAPIModelView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializator


class POSUserAPIModelView(viewsets.ModelViewSet):
    queryset = POSUser.objects.all()
    serializer_class = POSUserSerializator

# # стандартный метод вывода
# class GoodsApiView(APIView):
#     def get(self, request):
#         goods = Goods.objects.all().values()
#         goods_serialized = GoodSerializator(goods, many=True).data
#         return Response({'posts': goods_serialized})
#
#     def post(self, request):
#         serializer = GoodSerializator(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # new_good = Goods.objects.create(
#         #     barcode=request.data['barcode'],
#         #     name=request.data['name'],
#         #     price=request.data['price'],
#         #     supplier_id=[UUID('supplier_id')],
#         #     category_id=[UUID('category_id')],
#         # )
#         return Response({'post': 'GoodSerializator(new_good).data'})


# # Ручное прописывание всех методов
# class OrganizationApiView(APIView):
#     def get(self, request):
#         organizations = Organization.objects.all().values()
#         org_serialized = OrganizationSerializator(organizations, many=True).data
#         return Response({'posts': org_serialized})
#
#     def post(self, request):
#         serializer = OrganizationSerializator(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Put is not allowed"})
#         try:
#             intance = Organization.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object is not exist"})
#
#         serializer = OrganizationSerializator(data=request.data, instance=intance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Delete is not allowed"})
#         try:
#             instance = Organization.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object is not exist"})
#         instance.delete()
#         return Response({'post': 'deleted'})


# # ручная обработка данных для стандартного API
# class POSUserApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             users = POSUser.objects.all().values()
#             users_serialized = POSUserSerializator(users, many=True).data
#             return Response({'posts': users_serialized})
#         user = POSUser.objects.get(pk=pk)
#         user_serialized = POSUserSerializator(user).data
#         return Response({'posts': user_serialized})
#
#
# # Представление для листов и создания новых объектов(get, post)
# class POSUserAPIList(generics.ListCreateAPIView):
#     queryset = POSUser.objects.all()
#     serializer_class = POSUserSerializator
#
#
# # представление для чтения объекта, update и delete(get, put, delete)
# class POSUserAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = POSUser.objects.all()
#     serializer_class = POSUserSerializator
