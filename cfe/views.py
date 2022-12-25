from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
import random
from .models import (
    Item, HeroSlider, ItemCategory, ItemImage, ItemHighlights
    
)
from django.http import JsonResponse

class HomeLandingView(generic.View):
    template_name = "index.html"
    model = Item
    
    def get(self, request, *args, **kwargs):
        context = {
            "slider":HeroSlider.objects.all(), 
            "product": random.sample(list(Item.objects.all()), k=Item.objects.all().count()),
            "productg":random.sample(list(Item.objects.all()), k=Item.objects.all().count()),
            "productb":random.sample(list(Item.objects.all()), k=Item.objects.all().count()),
            "categories": ItemCategory.objects.all(),
            }
        return render(request, self.template_name, context)
    
    
home_landing_view = HomeLandingView.as_view()

class ProductDetailView(generic.View):
    template_name = "product_detail.html"
    model = Item
    
    def get(self, *args, **kwargs):
        item = get_object_or_404(self.model, slug=kwargs.get("slug"))
        context = {
            "item": item,
            "item_images": ItemImage.objects.filter(item=item).all(),
            "item_hightlight": ItemHighlights.objects.filter(item=item).all()
        }
        return render(self.request, self.template_name, context)
    
product_detail_view = ProductDetailView.as_view()


class CategoryDetailView(generic.View):
    template_name = "category_detail.html"
    model = ItemCategory
    
    def get(self, *args, **kwargs):
        category = get_object_or_404(self.model, name=kwargs.get("name"))
        context = {
            "category": category,
            "items": Item.objects.filter(category=category.id),
        }
        return render(self.request, self.template_name, context)

category_detail_view = CategoryDetailView.as_view()

def delivery_location(self):
    return JsonResponse({"location": DeliveryLocation.objects.all()}),