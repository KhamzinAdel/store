from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = "products"
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class Search(ListView):
    paginate_by = 3
    template_name = 'products/products.html'

    def get_queryset(self):
        value = self.request.GET.get('val')
        return Product.objects.filter(Q(name__contains=value) | Q(description__contains=value))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val'] = self.request.GET.get('val')
        return context
