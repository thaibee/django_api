import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from izoor.models import Goods

 # Первая версия сериализатора из модели
# class GoodsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Goods
#         fields = ('barcode', 'name', 'category')


#Ручная сериализация
# class GoodsModel:
#     def __init__(self, barcode, name, price):
#         self.barcode = barcode
#         self.name = name
#         self.price = price
# class GoodsSerializer(serializers.Serializer):
#     barcode = serializers.CharField(max_length=12)
#     name = serializers.CharField(max_length=20)
#     price = serializers.DecimalField(max_digits=12, decimal_places=4)
# def encode():
#     model = GoodsModel('123', 'banka supa', 20.1)
#     model_sr = GoodsSerializer(model)
#     print(model_sr.data, type(model_sr), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
# def decode():
#     stream = io.BytesIO(b'{"barcode":"23425","name":"test4","price":"2"}')
#     data = JSONParser().parse(stream)
#     serializer = GoodsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#     print(serializer.errors)

class GoodSerializator(serializers.Serializer):
    barcode = serializers.CharField(max_length=15)
    name = serializers.CharField(max_length=50)
    price = serializers.DecimalField(max_digits=19, decimal_places=4)
    category_id = serializers.CharField(max_length=36)
    supplier_id = serializers.CharField(max_length=36)
