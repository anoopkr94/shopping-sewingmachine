from django.contrib import admin
from .models import item, order_item, order, category, cartitem, service_register


class productAdmin(admin.ModelAdmin):
    list_display = ('name','brand','model_no','price')

class cartitem_admin(admin.ModelAdmin):
    list_display = ('user','item','quantity')

admin.site.register(item,productAdmin)
admin.site.register(order_item)
admin.site.register(order)
admin.site.register(service_register)
admin.site.register(category)
admin.site.register(cartitem,cartitem_admin)
# Register your models here.
