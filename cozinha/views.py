from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Product, Table
from .forms import ProductForm, TableForm
from django.urls import reverse
class ProductListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'cozinha/products/list_view.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).order_by('name')
        return queryset
        return queryset


class ComidasListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'cozinha/products/list_view/list_comidas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='1').order_by('name')
        return queryset

    
class BebidasListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'cozinha/products/list_view/list_comidas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='2').order_by('name')
        return queryset


class SobremesasListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'cozinha/products/list_view/list_sobremesas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True, type='3').order_by('name')
        return queryset


class ProductUpdateView(UpdateView):
    """
        View para alteração das informações de um produto existente.
    """

    model = Product
    form_class = ProductForm
    template_name = 'cozinha/products/update_view.html'

    def get_form_kwargs(self):
        kwargs = super(ProductUpdateView, self).get_form_kwargs()
        return kwargs

    def get_success_url(self):
        return reverse("cozinha:products")
class ProductDisableView(DeleteView):
    """
        View para deletar um produto existente.
    """

    model = Product
    template_name = 'cozinha/products/disable_view.html'

    def get_object(self):
        obj = super(ProductDisableView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("cozinha:products")

class ProductCreateView(CreateView):
    """1
        View para criação de um produto.
    """

    model = Product
    form_class = ProductForm
    template_name = 'cozinha/products/create_view.html'

    def get_form_kwargs(self):
        kwargs = super(ProductCreateView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cozinha:products")


class ProductDetailView(DetailView):
    """
        View para exibir detalhes de um produto existente.
    """
    model = Product
    template_name = 'cozinha/products/detail_view.html'

    def get_object(self):
        obj = super(ProductDetailView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse("cozinha:products")

class TableListView(ListView):
    """
        View para a listagem de mesas existentes.
    """

    model = Table
    template_name = 'cozinha/tables/list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Tables = Table.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        queryset = Table.objects.filter(is_active=True).order_by('number')
        return queryset
class TableUpdateView(UpdateView):
    """
        View para alteração das informações de um produto existente.
    """

    model = Table
    form_class = TableForm
    template_name = 'cozinha/tables/update_view.html'

    def get_form_kwargs(self):
        kwargs = super(TableUpdateView, self).get_form_kwargs()
        return kwargs

    def get_success_url(self):
        return reverse("cozinha:tables")
class TableDisableView(DeleteView):
    """
        View para deletar uma mesa existente.
    """

    model = Table
    template_name = 'cozinha/tables/disable_view.html'

    def get_object(self):
        obj = super(TableDisableView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("cozinha:tables")

class TableCreateView(CreateView):
    """
        View para criação de uma mesa.
    """

    model = Table
    form_class = TableForm
    template_name = 'cozinha/tables/create_view.html'

    def get_form_kwargs(self):
        kwargs = super(TableCreateView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cozinha:tables")
class TableDetailView(DetailView):
    """
        View para exibir detalhes de uma mesa existente.
    """
    model = Table
    template_name = 'cozinha/tables/detail_view.html'

    def get_object(self):
        obj = super(TableDetailView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse("cozinha:tables")

