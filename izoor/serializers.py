from rest_framework import serializers

from izoor.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('barcode', 'name', 'category')

