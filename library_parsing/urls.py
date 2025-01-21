from django.urls import path
from . import views

urlpatterns = [
   path('parse_list/', views.BookListView.as_view(), name='parse_list'),
   path('parse_form/', views.BookFormView.as_view(), name='parse_form'),
]