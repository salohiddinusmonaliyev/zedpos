from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Sell)
admin.site.register(SellItem)
admin.site.register(Purchase)
admin.site.register(Cost)
admin.site.register(CostCategory)
