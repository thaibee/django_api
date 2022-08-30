from django.contrib import admin

# Register your models here.
from izoor.models import *


@admin.register(POSRight)
class POSRightAdmin(admin.ModelAdmin):
    list_display = ('right', 'description')


admin.site.register(Goods)
admin.site.register(Wristband)
admin.site.register(GoodsCategory)
admin.site.register(Supplier)
admin.site.register(Organization)
admin.site.register(POSUser)
admin.site.register(Women)
admin.site.register(Category)
