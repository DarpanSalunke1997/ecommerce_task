from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SeasonalProductViewSet, BulkProductViewSet, DiscountViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'seasonal-products', SeasonalProductViewSet)
router.register(r'bulk-products', BulkProductViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
