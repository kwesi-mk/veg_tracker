from rest_framework.routers import DefaultRouter
from .views import VegetableViewSet, OrderViewSet, BuyerViewSet, FarmerViewSet, DriverViewSet

router = DefaultRouter()
router.register(r'vegetables', VegetableViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'buyers', BuyerViewSet)
router.register(r'farmers', FarmerViewSet)
router.register(r'drivers', DriverViewSet)

urlpatterns = router.urls