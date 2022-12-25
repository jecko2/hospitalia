from django import forms
from .models import ClientPurchase
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Jeckonia"
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Onyango"
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "devbyjeckonia@djp.inc"
    }))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "0700000000"
    }))
    class Meta:
        model = ClientPurchase
        fields = "__all__"

        
