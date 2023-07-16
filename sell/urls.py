from django.urls import path

from .views import *

urlpatterns = [
    path('cost-list/', cost_list),
    path('cost-add/', cost_create),
    path('list/', sale_list),
    path('add/<int:s>/', sale_add),
    path('add/', sale_create),
    path('<int:saleid>/delete/<int:id>/', saleitem_delete),
    path('<int:saleid>/add/', saleitem_create),
    path('<int:saleid>/checkout/', checkout),
    path('<int:saleid>/delete/', sale_delete),
    path('<int:saleid>/refresh/<int:tp>/', refresh),
    path('<int:s>/items/', saleitem_list),
    path('<int:sale>/return/<int:saleitem_id>/', return_create, name='return-add'),
    path('return/', return_list),
    path('category/', category),
    path('<int:sale_id>/minus/<int:saleitem_id>/', minus),
    path('<int:sale_id>/plus/<int:saleitem_id>/', plus),
    path('<int:sale_id>/quantity/<int:saleitem_id>/', quantity),
]