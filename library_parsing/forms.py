from django import  forms
from  . import models, parsing

class ParserForm(forms.Form):
   MEDIA_CHOICES = (
      ('litres', 'litres'),
      ('ts', 'ts'),
   )
   media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
   class Meta:
      fields = [
         'media_type',
      ]
       
   def parser_data(self):
      if self.data['media_type'] == 'litres':
         file_litres = parsing.parsing()
         for i in file_litres:
            models.BookParser.objects.create(**i)