from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register("new-product", NewProductViewSet, basename="newproduct")
urlpatterns = router.urls
