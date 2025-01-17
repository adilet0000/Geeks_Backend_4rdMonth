from django.urls import path
from . import views

urlpatterns = [
   path('all_books/', views.AllBooksView.as_view(), name='all_books'),
   path('drama_books/', views.DramaBooksView.as_view(), name='drama_books'),
   path('fiction_books/', views.FictionBooksView.as_view(), name='fiction_books'),
   path('fairy_books/', views.FairyBooksView.as_view(), name='fairy_books'),
]