import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.validators import UniqueValidator

from izoor.models import Goods, Organization, POSUser, POSRight


# Первая версия сериализатора из модели
# class GoodsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Goods
#         fields = ('barcode', 'name', 'category')


# Ручная сериализация
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


# #Вторая версия сериализатора с проверками и т.д.
# class GoodSerializator(serializers.Serializer):
#     barcode = serializers.CharField(max_length=15)
#     name = serializers.CharField(max_length=50)
#     price = serializers.DecimalField(max_digits=19, decimal_places=4)
#     category_id = serializers.CharField(max_length=36)
#     supplier_id = serializers.CharField(max_length=36)


# # в ручную написанный сериализатор
# class OrganizationSerializator(serializers.Serializer):
#     name = serializers.CharField(max_length=200, trim_whitespace=True,
#                                  validators=[UniqueValidator(queryset=Organization.objects.all())])
#     address = serializers.CharField(max_length=200)
#     overdraft = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Organization.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.address = validated_data.get("address", instance.address)
#         instance.overdraft = validated_data.get("overdraft", instance.overdraft)
#         instance.save()
#         return instance


class GoodSerializator(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    supplier = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Goods
        fields = '__all__'
        # fields = ("barcode", "name", "price", "category", "supplier")


class OrganizationSerializator(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        # fields = ("name",)


class POSUserSerializator(serializers.ModelSerializer):
    class Meta:
        model = POSUser
        # fields = '__all__'
        fields = ("name", "user_id", "pin", "right")
