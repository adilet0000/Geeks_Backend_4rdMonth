from django.db import models

class Tag(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name
    
class Product(models.Model):
   name = models.CharField(max_length=100, verbose_name='Название книги')
   price = models.PositiveIntegerField(default=100, verbose_name='Цена')
   tags = models.ManyToManyField(Tag, verbose_name='Тэг')

   def __str__(self):
      return self.name
