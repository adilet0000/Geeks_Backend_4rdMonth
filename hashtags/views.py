from django.shortcuts import render
from . import models
from django.views.generic import ListView

# общий список
class AllBooksView(ListView):
    template_name = 'hashtags/all_books.html'
    context_object_name = 'all_books'
    model = models.Product.objects.all()

    def get_queryset(self):
        return self.model
     
# def all_books(request):
#    if request.method == "GET":
#       all_books = models.Product.objects.all()
#       context = {'all_books': all_books}
#       return render(request, template_name='hashtags/all_books.html',
#          context=context)
      
      
      
class FairyBooksView(ListView):
    template_name = 'hashtags/fairy_books.html'
    context_object_name = 'fairy_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Сказки')
     
# def fairy_books(request):
#    if request.method == "GET":
#       fairy_books = models.Product.objects.filter(tags__name='Сказки')
#       context = {'fairy_books': fairy_books}
#       return render(request, template_name='hashtags/fairy_books.html',
#          context=context)



class FictionBooksView(ListView):
    template_name = 'hashtags/fiction_books.html'
    context_object_name = 'fiction_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Фантастика')
     
# def fiction_books(request):
#    if request.method == "GET":
#       fiction_books = models.Product.objects.filter(tags__name='Фантастика')
#       context = {'fiction_books': fiction_books}
#       return render(request, template_name='hashtags/fiction_books.html',
#          context=context)



class DramaBooksView(ListView):
    template_name = 'hashtags/drama_books.html'
    context_object_name = 'drama_books'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Драма')
     
# def drama_books(request):
#    if request.method == "GET":
#       drama_books = models.Product.objects.filter(tags__name='Драма')
#       context = {'drama_books': drama_books}
#       return render(request, template_name='hashtags/drama_books.html',
#          context=context) 