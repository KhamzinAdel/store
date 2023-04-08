from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import Product, ProductCategory
from .services import cashes_product


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
        queryset = Product.objects.filter(category_id=category_id).select_related('category') \
            if category_id else Product.objects.all().select_related('category')
        products = cashes_product('products', queryset, 30)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = ProductCategory.objects.values('id', 'name')
        categories = cashes_product('categories', queryset, 30)
        context['categories'] = categories
        return context


class SearchView(ListView):
    paginate_by = 3
    template_name = 'products/products.html'

    def get_queryset(self):
        value = self.request.GET.get('val')
        return Product.objects.filter(Q(name__contains=value) | Q(description__contains=value))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val'] = self.request.GET.get('val')
        return context
