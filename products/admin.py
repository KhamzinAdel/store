from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'get_image')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'category', 'get_image')
    readonly_fields = ('description', 'get_image')
    search_fields = ('name',)
    ordering = ('name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0


admin.site.site_title = 'Store'
admin.site.site_header = 'Store'
