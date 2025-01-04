from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
   return HttpResponse("Я разработчик, в текущий момент учу Django!✌")

def about_my_pets(request):
   return HttpResponse("У нет и никогда не было домашних животных. Я считаю что это тяжкий труд и большая ответственность.🤷‍♂️")

def date_time(request):
   current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
   return HttpResponse(f"Текущее системное время: {current_time} 👀")