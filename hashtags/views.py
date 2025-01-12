from django.shortcuts import render
from . import models

# общий список
def all_books(request):
   if request.method == "GET":
      all_books = models.Product.objects.all()
      context = {'all_books': all_books}
      return render(request, template_name='hastags/all_books.html',
         context=context)

def fairy_books(request):
   if request.method == "GET":
      fairy_books = models.Product.objects.filter(tags__name='Напитки')
      context = {'fairy_books': fairy_books}
      return render(request, template_name='hastags/fairy_books.html',
         context=context)

def fiction_books(request):
   if request.method == "GET":
      fiction_books = models.Product.objects.filter(tags__name='Еда')
      context = {'fiction_books': fiction_books}
      return render(request, template_name='hastags/fiction_books.html',
         context=context)
       
def drama_books(request):
   if request.method == "GET":
      drama_books = models.Product.objects.filter(tags__name='Еда')
      context = {'drama_books': drama_books}
      return render(request, template_name='hastags/drama_books.html',
         context=context) 