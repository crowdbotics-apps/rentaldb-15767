from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddressViewSet, UnitViewSet

router = DefaultRouter()
router.register("address", AddressViewSet)
router.register("unit", UnitViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
