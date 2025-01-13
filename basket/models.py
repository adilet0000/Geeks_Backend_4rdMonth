from django.db import models
from library.models import Book

class OrderModel(models.Model):
   
   name = models.CharField(max_length=50, verbose_name='Укажите ваше имя')
   phone_number = models.CharField(max_length=15, verbose_name='Укажите номер вашего телефона')
   choice_book = models.ForeignKey(Book, on_delete=models.CASCADE)
   email = models.EmailField(verbose_name='Укажите свою почту(необязательно)', blank=True)
   address = models.TextField(verbose_name='Укажите адрес доставки')
   
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
      return f'{self.name}-{self.choice_book}'