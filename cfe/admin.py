from django.contrib import admin
from .models import (
    HeroSlider,
    Item, ItemCategory, ItemHighlights, Review, ItemImage, 
)

@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'file_size']


class ItemImageInline(admin.StackedInline):
    model = ItemImage
    extra = 1
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ("name", "name2")
    list_display = [
        'name', 'name2', 'category', 'availability',
        'price', 'dicount_price', 'selling_price', 
        'rating'
        ]
    prepopulated_fields = {"slug": ('name', )}
    inlines = [ItemImageInline,]

@admin.register(ItemCategory)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(ItemHighlights)
class HighLightsAdmin(admin.ModelAdmin):
    list_display = ['item', 'highlight']


