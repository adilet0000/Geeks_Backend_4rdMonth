from django.urls import path
from . import views

urlpatterns = [
   path('all_books/', views.all_books, name='all_books'),
   path('drama_books/', views.drama_books, name='drama_books'),
   path('fiction_books/', views.fiction_books, name='fiction_books'),
   path('fairy_books/', views.fairy_books, name='fairy_books'),
]