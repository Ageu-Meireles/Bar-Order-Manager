from django.urls import path
from . import views

app_name = "establishment"

urlpatterns = [
    path('produtos', views.ProductListView.as_view(), name='products'),
    path('produtos/comidas', views.ComidasListView.as_view(), name='products-1'),
    path('produtos/bebidas', views.BebidasListView.as_view(), name='products-2'),
    path('produtos/sobremesas', views.SobremesasListView.as_view(), name='products-3'),
    path('produtos/criar', views.ProductCreateView.as_view(), name='product-add'),
    path('produtos/editar/<int:pk>', views.ProductUpdateView.as_view(), name='product-edit'),
    # path('produtos/deletar/<int:pk>', views.ProductDeleteView.as_view(), name='product-delete'),
    path('produtos/detalhes/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('produtos/desativar/<int:pk>', views.ProductDisableView.as_view(), name='product-disable'),

    path('mesas', views.TableListView.as_view(), name='tables'),
    path('mesas/criar', views.TableCreateView.as_view(), name='table-add'),
    path('mesas/editar/<int:pk>', views.TableUpdateView.as_view(), name='table-edit'),
    # path('mesas/deletar/<int:pk>', views.TableDeleteView.as_view(), name='table-delete'),
    path('mesas/detalhes/<int:pk>', views.TableDetailView.as_view(), name='table-detail'), 
    path('mesas/desativar/<int:pk>', views.TableDisableView.as_view(), name='table-disable'),
]