from django.db import models

class Genre(models.Model):
   name = models.CharField(max_length=100, verbose_name='Напишите название нового жанра')

   class Meta:
      verbose_name = 'Жанр'
      verbose_name_plural = 'Жанры'

   def __str__(self):
      return self.name


class Book(models.Model):
   cover = models.ImageField(upload_to='covers/', verbose_name='Загрузите обложку')
   title = models.CharField(max_length=100, verbose_name='Напишите название')
   description = models.TextField(verbose_name='Укажите описание')
   price = models.PositiveIntegerField(verbose_name='Укажите цену', default=350)
   release_date = models.DateTimeField(blank=True)
   added_at = models.DateTimeField(auto_now_add=True)

   genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1, verbose_name='Выберите жанр')
   
   author = models.CharField(max_length=100, verbose_name='Укажите автора', default='Автор не указан')
   author_email = models.EmailField(default='Почта автора не указана', verbose_name='Укажите почту автора', blank=True)
   review = models.URLField(verbose_name='укажите ссылку с YOUTUBE')

   class Meta:
      verbose_name = 'Книга'
      verbose_name_plural = 'Список книг'

   def __str__(self):
      return f'{self.title} - {self.author}'