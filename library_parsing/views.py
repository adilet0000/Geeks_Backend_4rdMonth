from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms
from django.views import generic

class BookListView(generic.ListView):
    template_name = 'parsing/parse_list.html'
    context_object_name = 'parse'
    model = models.BookParser

    def get_queryset(self):
        return self.model.objects.all()

class BookFormView(generic.FormView):
    template_name = 'parsing/parse_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсинг успешно завершен')
        else:
            return super(BookFormView, self).post(request, *args, **kwargs)