from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import ClientPurchase
from .forms import CheckoutForm
from cfe.models import Item
from django_daraja.views import MpesaClient
from django.http import HttpResponse
import math

# Create your views here.

class CheckoutItemView(generic.View):
    template_name = "checkout.html"
    model = ClientPurchase
    checkout_form = CheckoutForm
    success_url = "cfe:home"
    client = MpesaClient()
    
    def get(self, *args, **kwargs):
        context = {
            "form": self.checkout_form(),
        }
        return render(self.request, self.template_name, context)
    
    def post(self, *args, **kwargs):
        item = get_object_or_404(Item, slug=kwargs.get("slug"))
        form = self.checkout_form(self.request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.item = item
            amount = math.ceil(instance.item.get_discounted_price())
            instance.save()
            item.quantity -= 1
            item.save()
            form.save()
            if form.cleaned_data['phone'] is not None:
                callback_url=self.request.build_absolute_uri(
                        reverse("checkout:mpesa_stk_push_callback")
                    )
                self.client.stk_push(
                    phone_number=str(form.cleaned_data['phone']),
                    amount=amount,
                    account_reference="reference",
                    transaction_desc="description",
                    callback_url=callback_url
                )
                return redirect(callback_url)
            return HttpResponse("Thanks for purchasing our items")
        return redirect(self.success_url)
    
product_checkout_view = CheckoutItemView.as_view()



def mpesa_callback(request):
    return render(request, "thank.html")
