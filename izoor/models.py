from django.urls import reverse

from api.mssql_uuid import MssqlUUID
from django.db import models


class Wristbands(models.Model):
    id = models.CharField(db_column='Wrist_NUM', primary_key=True, max_length=10, editable=False, default=None)
    balance = models.DecimalField(db_column='Top_up_rest', max_digits=19, decimal_places=4, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('wristbands', kwargs={"slug": self.slug})

    def __str__(self):
        return self.id

    # def get_countries(self):
    #     return self.org_country

    class Meta:
        managed = False
        db_table = 'Wristbands'
        ordering = ['id']


class Goods(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='goodsID', max_length=36, editable=False,
                     default=None)
    barcode = models.CharField(db_column='goods_code', unique=False, max_length=15, verbose_name='Barcode', blank=False,
                               null=False)
    name = models.CharField(db_column='goods_name', unique=False, max_length=50, verbose_name='Name', blank=False,
                            null=False)
    price = models.DecimalField(db_column='goods_price', max_digits=19, decimal_places=4, blank=False, null=False)

    category = models.ForeignKey(db_column='Goods_CategoryId', to_field='slug', to='GoodsCategory',
                                 on_delete=models.PROTECT, null=False)
    supplier = models.ForeignKey(db_column='SupplierID', to_field='slug', to='Supplier',
                                 on_delete=models.PROTECT, null=False)

    def get_absolute_url(self):
        return reverse('goods', kwargs={"slug": self.slug})

    def __str__(self):
        return self.barcode + '  name: ' + self.name

    # def get_countries(self):
    #     return self.org_country

    class Meta:
        managed = False
        db_table = 'GoodsPrices'
        ordering = ['barcode']


class GoodsCategory(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='Goods_CategoryId', max_length=36, editable=False, default=None)
    name = models.CharField(db_column='Goods_Category', unique=False, max_length=20, verbose_name='Category',
                            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Goods_Category'
        ordering = ['name']


class Supplier(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='SupplierID', max_length=36, editable=False, default=None)
    name = models.CharField(db_column='Org_Name', unique=False, max_length=20, verbose_name='Supplier',
                            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Supplier'
        ordering = ['name']


class Organization(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='OrganizationID', max_length=36, editable=False, default=None)
    name = models.CharField(db_column='Org_Name', unique=True, max_length=200, verbose_name='Company')
    address = models.CharField(db_column='Org_Address', blank=True, null=False, max_length=200)
    overdraft = models.BooleanField(db_column='CanOverdraft')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'Organization'
        ordering = ['name']


class POSUser(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='UserID', max_length=36, editable=False, default=None)
    user_id = models.CharField(db_column='EmpID', unique=True, max_length=5)
    name = models.CharField(db_column='UserName', unique=True, max_length=50)
    right = models.ForeignKey(db_column='ListRight', to_field='right', to='POSRight',
                              on_delete=models.PROTECT, null=False)
    pin = models.IntegerField(db_column='Pin')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'LocalUsers'
        ordering = ['user_id']


class POSRight(models.Model):
    right = models.CharField(primary_key=True, db_column='ListRight', max_length=36, editable=False)
    description = models.CharField(db_column='Description', max_length=50)

    def __str__(self):
        return self.right

    class Meta:
        managed = False
        db_table = 'LocalUserRight'
        ordering = ['right']
