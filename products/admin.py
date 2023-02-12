from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    ordering = ('name', )


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0

