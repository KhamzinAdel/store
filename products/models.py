import stripe
from django.conf import settings
from django.db import models
from django.urls import reverse

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class GeneralProduct(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductCategory(GeneralProduct):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.name


class Product(GeneralProduct):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

    def __str__(self):
        return f'Продукты: {self.name} │ Категория: {self.category.name}'

    def save(self, *args, **kwargs):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super().save(*args, **kwargs)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='rub')
        return stripe_product_price
