from django.contrib import admin
from .models import ClientPurchase

@admin.register(ClientPurchase)
class ClientPurchaseAdmin(admin.ModelAdmin):
    list_display = ['item', 'first_name', 'last_name', 'phone']
    