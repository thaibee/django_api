from django.urls import reverse

from api.mssql_uuid import MssqlUUID
from django.db import models


class Wristband(models.Model):
    slug = models.CharField(db_column='Wrist_Num', max_length=10, editable=False, default=None)
    balance = models.DecimalField(db_column='Top_up_rest', max_digits=19, decimal_places=4, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('org_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return 'W.' + self.slug

    # def get_countries(self):
    #     return self.org_country

    class Meta:
        managed = False
        db_table = 'Wristbands'
        # ordering = ['org_name']


class Goods(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='goodsID', max_length=36, editable=False,
                     default=None)
    barcode = models.CharField(db_column='goods_code', unique=False, max_length=15, verbose_name='Barcode', blank=False,
                               null=False)
    name = models.CharField(db_column='goods_name', unique=False, max_length=50, verbose_name='Name', blank=False,
                            null=False)
    price = models.DecimalField(db_column='goods_price', max_digits=19, decimal_places=4, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('goods', kwargs={"slug": self.slug})

    def __str__(self):
        return self.barcode+' : ' + self.name

    # def get_countries(self):
    #     return self.org_country

    class Meta:
        managed = False
        db_table = 'GoodsPrices'
        # ordering = ['org_name']
