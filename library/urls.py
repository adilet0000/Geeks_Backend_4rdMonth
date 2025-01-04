from django.urls import path
from .views import about_me, about_my_pets, date_time

urlpatterns = [
   path('about_me/', about_me, name='about_me'),
   path('about_my_pets/', about_my_pets, name='about_my_pets'),
   path('date_time/', date_time, name='date_time'),
]