from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Product, Table
from .forms import ProductForm, TableForm
from django.urls import reverse

class ProductListView(View):
    """
        View para a listagem das categorias dos produtos disponíveis.
        TODO: se possível incluir paginação
    """

    model = Product
    template_name = 'establishment/products/list_product_categories.html'
    # paginate_by = 10

    def get(self, request):
        return render(request, self.template_name)


class ComidasListView(ListView):
    """
        View para a listagem de comidas existentes.
    """

    model = Product
    template_name = 'establishment/products/list_foods.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='1').order_by('name')
        return queryset

    
class BebidasListView(ListView):
    """
        View para a listagem de comidas existentes.
    """

    model = Product
    template_name = 'establishment/products/list_foods.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='2').order_by('name')
        return queryset


class SobremesasListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'establishment/products/list_view/list_sobremesas.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='3').order_by('name')
        return queryset


class ProductUpdateView(UpdateView):
    """
        View para alteração das informações de um produto existente.
    """

    model = Product
    form_class = ProductForm
    template_name = 'establishment/products/update_product.html'

    def get_success_url(self):
        return reverse("establishment:products")


class ProductDisableView(DeleteView):
    """
        View para desativar um produto existente.
    """

    model = Product
    template_name = 'establishment/products/disable_product.html'

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).order_by('name')
        return queryset

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("establishment:products")


class ProductCreateView(CreateView):
    """
        View para criação de um produto.
    """

    model = Product
    form_class = ProductForm
    template_name = 'establishment/products/create_product.html'

    def get_success_url(self):
        return reverse("establishment:products")


class ProductDetailView(DetailView):
    """
        View para exibir detalhes de um produto existente.
    """
    model = Product
    template_name = 'establishment/products/product_details.html'

    def get_success_url(self):
        return reverse("establishment:products")


class TableListView(ListView):
    """
        View para a listagem de mesas existentes.
    """

    model = Table
    template_name = 'establishment/tables/list_view.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Table.objects.filter(is_active=True).order_by('number')
        return queryset


class TableUpdateView(UpdateView):
    """
        View para alteração das informações de uma mesa existente.
    """

    model = Table
    form_class = TableForm
    template_name = 'establishment/tables/update_table.html'

    def get_success_url(self):
        return reverse("establishment:tables")


class TableDisableView(DeleteView):
    """
        View para desativar uma mesa existente.
    """

    model = Table
    template_name = 'establishment/tables/disable_table.html'

    def get_queryset(self):
        queryset = Table.objects.filter(is_active=True).order_by('number')
        return queryset

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("establishment:tables")

class TableCreateView(CreateView):
    """
        View para criação de uma mesa.
    """

    model = Table
    form_class = TableForm
    template_name = 'establishment/tables/create_table.html'

    def get_success_url(self):
        return reverse("establishment:tables")


class TableDetailView(DetailView):
    """
        View para exibir detalhes de uma mesa existente.
    """
    model = Table
    template_name = 'establishment/tables/table_details.html'

    def get_success_url(self):
        return reverse("establishment:tables")

