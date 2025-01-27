from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms

class RegisterView(generic.CreateView):
   form_class = forms.CustomEmployeeForm
   template_name = 'employee_finder/register.html'
   success_url = reverse_lazy('employee_finder:login')
    
class AuthLoginView(LoginView):
   template_name = 'employee_finder/login.html'
   form_class = AuthenticationForm
        
   def get_success_url(self):
      return reverse('employee_finder:user_list')

class AuthLogoutView(LogoutView):
   next_page = reverse_lazy('employee_finder:login')
    

class UserListView(generic.ListView):
   template_name = 'employee_finder/user_list.html'
   context_object_name = 'employee_finder'
   model = models.CustomEmployee
    
   def get_queryset(self):
      return self.model.objects.all().order_by('-id')