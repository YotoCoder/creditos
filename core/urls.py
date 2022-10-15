from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from cliente.views import ClienteViewSet
from producto.views import ProductoViewSet

from credito.views import CreditoViewSet, CancelCreditView, PayCreditView

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'credito', CreditoViewSet)
router.register(r'producto', ProductoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Cancel credit and Pay credit
    path('credito/cancel/<int:pk>/', CancelCreditView.as_view()),
    path('credito/pay/<int:pk>/', PayCreditView.as_view()),

    # Debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls