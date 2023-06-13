from django.urls import path

from .views import *

urlpatterns = [
    path('cost-list/', cost_list),
    path('cost-add/', cost_create),
    path('list/', sale_list),
    path('add/<int:s>/', sale_add),
    path('add/', create_sale),
    path('<int:saleid>/delete/<int:id>/', saleitem_delete),
    path('<int:saleid>/add/', saleitem_create),
    path('<int:saleid>/checkout/', checkout),
    path('<int:saleid>/delete/', sale_delete),
    path('<int:saleid>/refresh/<int:tp>/', refresh),
    path('<int:s>/items/', saleitem_list),
    path('returns/', return_list),
]