from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from .models import OrderModel


def create_order_view(request):
   if request.method == 'POST':
      form = forms.OrderForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('orders_list')
   else:
      form = forms.OrderForm()
   return render(request, template_name='orders/create_order.html',
      context={'form': form})


def orders_list_view(request):
   if request.method == 'GET':
      orders_list = models.OrderModel.objects.all().order_by("-id")
      context = {'orders_list': orders_list}
      return render(request, template_name='orders/orders_list.html',
         context=context)


def order_detail_view(request, id):
   if request.method == 'GET':
      order_id = get_object_or_404(models.OrderModel, id=id)
      context = {'order_id': order_id}
      return render(request, template_name='orders/order_detail.html',
         context=context)


def order_update_view(request, id):
   order_id = get_object_or_404(models.OrderModel, id=id)
   if request.method == 'POST':
      form = forms.OrderForm(request.POST, instance=order_id)
      if form.is_valid():
         form.save()
         return redirect('orders_list')
   else:
      form = forms.OrderForm(instance=order_id)
   return render(request, template_name='orders/update_order.html',
      context={'form': form, 'id': id})


def delete_order_view(request, id):
   order_id = get_object_or_404(models.OrderModel, id=id)
   order_id.delete()
   return redirect('orders_list')