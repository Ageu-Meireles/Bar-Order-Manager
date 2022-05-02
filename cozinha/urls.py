from django.urls import path
from . import views

app_name = "cozinha"

urlpatterns = [
    # Uma rota é um caminho para uma página que você acesssa através de uma URL
    # Rotas para acessar funções dos produtos
    path('produtos', views.ProductListView.as_view(), name='products'),      # Listar produto
    path('produtos/comidas', views.ComidasListView.as_view(), name='products-com'),      # Listar produto
    path('produtos/bebidas', views.BebidasListView.as_view(), name='products-beb'),      # Listar produto
    path('produtos/sobremesas', views.SobremesasListView.as_view(), name='products-sob'),      # Listar produto
    path('produtos/criar', views.ProductCreateView.as_view(), name='product-add'),       # Criar produto
    path('produtos/editar/<int:pk>', views.ProductUpdateView.as_view(), name='product-edit'),        # Editar produto
    # path('produtos/deletar/<int:pk>', views.ProductDeleteView.as_view(), name='product-delete'),     # Deletar produto
    path('produtos/detalhes/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),        # Visualizar detalhas do produto
    path('produtos/desativar/<int:pk>', views.ProductDisableView.as_view(), name='product-disable'),     # Desativar produto

    # Rotas para acessar funções das mesas
    path('mesas', views.TableListView.as_view(), name='tables'),       # Listar mesa
    path('mesas/criar', views.TableCreateView.as_view(), name='table-add'),      # Criar mesa
    path('mesas/editar/<int:pk>', views.TableUpdateView.as_view(), name='table-edit'),       # Editar mesa
    # path('mesas/deletar/<int:pk>', views.TableDeleteView.as_view(), name='table-delete'),        # Deletar mesa
    path('mesas/detalhes/<int:pk>', views.TableDetailView.as_view(), name='table-detail'),       # Visualizar detalhas da mesa
    path('mesas/desativar/<int:pk>', views.TableDisableView.as_view(), name='table-disable'),        # Desativar mesa
]