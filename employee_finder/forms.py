from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

GENDER = (
      ('M','Male'),
      ('F','Female')
   )

class CustomEmployeeForm(UserCreationForm):
   phone_number = forms.CharField(required=True, label='Введите номер телефона')
   experience = forms.IntegerField(required=True, label='Укажите ваш опыт (в годах)')
   age = forms.IntegerField(required=True, label='Возраст')
   gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')
    
   class Meta:
      model = models.CustomEmployee
      fields = (
         'username',
         'password1',
         'password2',
         'first_name',
         'last_name',
         'phone_number',
         'age',
         'gender',
         'experience'
      )
   def save(self, commit=True):
      user = super(CustomEmployeeForm, self).save(commit=False)
      user.phone_number = self.cleaned_data['phone_number']
      user.age = self.cleaned_data['age']
      user.gender = self.cleaned_data['gender']
      user.experience = self.cleaned_data['experience']
        
      if commit:
         user.save()
      return user
        