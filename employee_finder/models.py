from django.db import models
from django.contrib.auth.models import User

class CustomEmployee(User):
   GENDER = (
      ('M','Male'),
      ('F','Female')
   )
   
   phone_number = models.CharField(max_length=14)
   experience = models.PositiveIntegerField(default=1)
   age = models.PositiveIntegerField(default = 18)
   gender = models.CharField(max_length=1, choices=GENDER)
   salary = models.CharField(max_length=100)
   
   def save(self, *args, **kwargs):
      if self.experience < 1:
         self.salary = 500
      elif self.experience >=1 and self.experience < 3:
         self.salary = 1000
      elif self.experience >=3 and self.experience < 7:
         self.salary = 2000
      elif self.experience >=7 and self.experience <= 10:
         self.salary = 5000
      else:
         self.salary = 0
      super().save(*args, **kwargs)