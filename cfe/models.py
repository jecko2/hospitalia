from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import math

class ItemCategory(models.Model):
    name = models.CharField(_("DRUG CATEGORY"), max_length=60, unique=True)
    image = models.ImageField(upload_to="category/")
    
    def get_absolute_url(self):
        return reverse("cfe:category_detail", kwargs={"name": self.name})

    def __str__(self):
        return self.name  

class ItemImage(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="item_pic")
    picture = models.ImageField(upload_to="product/")
    
class ItemHighlights(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="item_highlight")
    highlight = models.CharField(_("DRUG HIGHLIGHT"), max_length=20, help_text="Generally Consumed With Water")

class Item(models.Model):
    name = models.CharField(_("GENERIC NAME"), max_length=110, unique=True)
    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)
    name2 = models.CharField(_("BRAND NAME"), max_length=60, blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="item_category")
    availability = models.BooleanField(default=True)
    pic = models.ImageField(upload_to="product/")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    dicount_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    rating = models.IntegerField(default=2)
    description = models.TextField(_("DRUG DESCRIPTION"), blank=True, null=True)
    quantity = models.IntegerField(default=1)
    

    def get_percentage_off(self):
        return math.trunc((self.dicount_price / self.price) * 100)
    def get_discounted_price(self):
        return self.price - self.dicount_price
    def is_discounted(self):
        if self.dicount_price > 0:
            return True
        return False
    def is_available(self):
        if self.quantity> 0:
            return True
        return False
    def get_avalable_count(self):
        return self.quantity
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    @property
    def selling_price(self):
        return self.get_discounted_price()
    
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        
    def get_absolute_url(self):
        return reverse("cfe:item_detail", kwargs={"slug": self.slug})
    
    def get_checkout_url(self):
        return reverse("checkout:checkout", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name 


class Review(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    review = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=2)
    
    
class HeroSlider(models.Model):
    slider = models.ImageField(upload_to="slider/")
    
    @property
    def file_name(self):
        return self.slider.name[7:-4].title()
    @property
    def file_size(self):
        return f"{self.slider.size} KB"
    
    def __str__(self):
        return f"{self.slider.name}"
    