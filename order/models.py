from django.db import models
from cfe.models import Item
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class ClientPurchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=225)
    phone = models.IntegerField(_("Phone Number"), blank=True, null=True)

    def __str__(self):
        return self.first_name
