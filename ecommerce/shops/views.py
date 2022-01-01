from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import UpdateView ,DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .forms import CreateShopForm
from .models import Shop
from django.views.generic.edit import CreateView

# Create your views here.


class DashboardView(LoginRequiredMixin, ListView):
    template_name = "adminshop/pages/shopslist.html"

    def get_queryset(self):
        return Shop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_list'] = Shop.objects.filter(author= self.request.user.id , is_delete=False)
        # context['shop_list'] = Shop.objects.all()
        # print( 'the user ', self.request.user)
        return context

class RenderConfirmDeleteShop(LoginRequiredMixin,DetailView):
    model=Shop
    template_name = "adminshop/pages/conform_deleteshop.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shop_detail"] =get_object_or_404(Shop,slug=self.kwargs['slug'] )
        return context

class RenderDeleteShop(LoginRequiredMixin,UpdateView):
    model=Shop
    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Shop,slug=self.kwargs['slug'])
        if object:
            object.is_delete=True
            object.save()
            return redirect(reverse('shops:dashboard_admin'))


class CreateShop(LoginRequiredMixin,View):
    form_class = CreateShopForm
    template_name="adminshop/forms/create_shop.html"
    def get(self, request):
        form = CreateShopForm()
        return render(request, 'adminshop/forms/create_shop.html',{'form': form})

    def post(self, request):
        obj = Shop.objects.filter(is_active=False ,author=request.user).count()
        if obj>0:
            return redirect(reverse('shops:dashboard_admin'))
        form = CreateShopForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('shops:dashboard_admin'))
