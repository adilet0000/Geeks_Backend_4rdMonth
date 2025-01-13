from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime

from .models import Book, Review
from .forms import CommentForm

from . import models

def book_list(request):
   if request.method == "GET":
      book_list = models.Book.objects.all().order_by('-id')
      context = { 'book_list': book_list }
      return render(request, template_name='book.html', context=context)


def book_detail(request, id):
   book = get_object_or_404(Book, id=id)
   
   if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.reviews_choice = book
         comment.save()
         return redirect('book_detail', id=book.id)
   else:
      form = CommentForm()
   
   reviews = Review.objects.filter(reviews_choice=book).order_by('-created_at')
   context = {
      'book_id': book,
      'form': form,
      'reviews': reviews,
   }
   return render(request, template_name='book_detail.html', context=context)














def about_me(request):
   return HttpResponse("Я разработчик, в текущий момент учу Django!✌")

def about_my_pets(request):
   return HttpResponse("У нет и никогда не было домашних животных. Я считаю что это тяжкий труд и большая ответственность.🤷‍♂️")

def date_time(request):
   current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
   return HttpResponse(f"Текущее системное время: {current_time} 👀")