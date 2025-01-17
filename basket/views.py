from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . import models, forms
from .models import OrderModel



class CreateOrderView(generic.CreateView):
   template_name = 'orders/create_order.html'
   form_class = forms.OrderForm
   success_url = '/orders_list/'
   
   def form_valid(self, form):
      print(form.cleaned_data)
      return super(CreateOrderView, self).form_valid(form=form)

# def create_order_view(request):
#    if request.method == 'POST':
#       form = forms.OrderForm(request.POST, request.FILES)
#       if form.is_valid():
#          form.save()
#          return redirect('orders_list')
#    else:
#       form = forms.OrderForm()
#    return render(request, template_name='orders/create_order.html',
#       context={'form': form})


class OrdersListView(generic.ListView):
   template_name = 'orders/orders_list.html'
   model = models.OrderModel
   
   def get_queryset(self):
      return self.model.objects.all().order_by('-id')

# def orders_list_view(request):
#    if request.method == 'GET':
#       orders_list = models.OrderModel.objects.all().order_by("-id")
#       context = {'orders_list': orders_list}
#       return render(request, template_name='orders/orders_list.html',
#          context=context)


class OrderDetailView(generic.DetailView):
   template_name = 'orders/order_detail.html'

   def get_object(self, **kwargs):
      order_id = self.kwargs.get('id')
      return get_object_or_404(models.OrderModel, id=order_id)

# def order_detail_view(request, id):
#    if request.method == 'GET':
#       order_id = get_object_or_404(models.OrderModel, id=id)
#       context = {'order_id': order_id}
#       return render(request, template_name='orders/order_detail.html',
#          context=context)


class OrderUpdateView(generic.UpdateView):
   template_name = 'orders/update_order.html'
   form_class = forms.OrderForm
   success_url = '/orders_list/'
   def get_object(self, **kwargs):
      order_id = self.kwargs.get('id')
      return get_object_or_404(models.OrderModel, id=order_id)
   def form_valid(self, form):
      print(form.cleaned_data)
      return super(OrderUpdateView, self).form_valid(form=form)

# def order_update_view(request, id):
#    order_id = get_object_or_404(models.OrderModel, id=id)
#    if request.method == 'POST':
#       form = forms.OrderForm(request.POST, instance=order_id)
#       if form.is_valid():
#          form.save()
#          return redirect('orders_list')
#    else:
#       form = forms.OrderForm(instance=order_id)
#    return render(request, template_name='orders/update_order.html',
#       context={'form': form, 'id': id})


class DeleteOrderView(generic.DeleteView):
    template_name = 'orders/confirm_delete.html'
    success_url = '/orders_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderModel, id=order_id)

# def delete_order_view(request, id):
#    order_id = get_object_or_404(models.OrderModel, id=id)
#    order_id.delete()
#    return redirect('orders_list')