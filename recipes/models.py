from django.db import models

class Recipe(models.Model):
   title = models.CharField(max_length=255, verbose_name="Название рецепта")
   description = models.TextField(verbose_name="Описание рецепта")

   def __str__(self):
      return self.title

class Ingredient(models.Model):
   UNITS = [
      ('г', 'граммы'),
      ('кг', 'килограммы'),
      ('мл', 'миллилитры'),
      ('л', 'литры'),
      ('шт', 'штуки'),
   ]

   name = models.CharField(max_length=255, verbose_name="Название ингредиента")
   quantity = models.FloatField(verbose_name="Количество")
   unit = models.CharField(max_length=10, choices=UNITS, verbose_name="Единица измерения")
   recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

   def __str__(self):
      return f"{self.name} ({self.quantity} {self.unit})"
