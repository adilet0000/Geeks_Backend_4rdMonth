from django import forms
from .models import Review

class CommentForm(forms.ModelForm):
   class Meta:
      model = Review
      exclude = ['reviews_choice', 'created_at'] # то что не надо
