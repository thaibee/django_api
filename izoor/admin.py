from django.contrib import admin

# Register your models here.
from izoor.models import *
admin.site.register(Goods)
admin.site.register(Wristbands)
admin.site.register(GoodsCategory)
admin.site.register(Supplier)
