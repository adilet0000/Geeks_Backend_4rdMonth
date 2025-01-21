from django.db import models

class BookParser(models.Model):
   info = models.CharField(max_length=250)
   href = models.URLField()
    
   def __str__(self):
      return self.href