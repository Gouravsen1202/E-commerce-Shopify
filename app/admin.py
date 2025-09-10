from django.contrib import admin
from .models import Customer,Query,DynamicCards,ProductOrderDetailAfterPayment
# Register your models here.

admin.site.register(Customer)
admin.site.register(Query)
admin.site.register(DynamicCards)
admin.site.register(ProductOrderDetailAfterPayment)