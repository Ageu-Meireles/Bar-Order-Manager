from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Session
from .forms import SessionForm
from django.urls import reverse

class HomePageView(CreateView):
    """
        View para iniciar a sessão de um cliente no bar.
    """
    template_name = "home.html"
    model = Session
    form_class = SessionForm

    def get_form_kwargs(self):
        kwargs = super(HomePageView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        form.instance.is_busy = True
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("cozinha:products")