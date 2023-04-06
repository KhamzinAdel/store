from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import IndexView

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('captcha/', include('captcha.urls')),
    path('orders/', include('orders.urls', namespace='orders')),

    path('api/v1/', include('api.urls', namespace='api')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += i18n_patterns(
    path('118n/', include('django.conf.urls.i18n')),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('basket/', include('basket.urls', namespace='basket')),
)

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
