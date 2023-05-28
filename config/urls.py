"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from product.views import *
from clients.views import *
from sell.views import *
from partner.views import *
from accounts.views import *
from app.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register("warehouse", WarehouseViewSet, basename="warehouse")
router.register("measure", MeasureViewSet, basename="measure")
router.register("client", ClientViewSet, basename="client")
router.register('sell', SellViewSet, basename="sell")
router.register("dealer", DealerViewSet, basename="dealer")
router.register("cost", CostViewSet, basename="cost")
router.register('staff', UserViewSet, basename="staff")




schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("payment/", PaymentView.as_view()),
    path("hisob/<int:a>/", Hisoblash.as_view()),
    path("home/<str:a>/<str:b>/", MainView.as_view()),
    path("home/", MainView.as_view()),
    path("sell-item/", SellItemViewSet.as_view()),
    path("new-product/<int:p>/<int:q>/", NewProduct.as_view()),
    path("archive/", Archive.as_view()),
    path("pay-client/", ClientPayView.as_view()),
]
