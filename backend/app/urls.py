# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SliderViewSet, ServiceViewSet, ProductViewSet, CartViewSet, UserViewSet

router = DefaultRouter()
router.register(r'sliders', SliderViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
