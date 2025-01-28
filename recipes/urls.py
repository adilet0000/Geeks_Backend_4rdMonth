from django.urls import path
from . import views

urlpatterns = [
   path('', views.recipe_list, name='recipe_list'),
   path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
   path('create/', views.create_recipe, name='create_recipe'),
   path('recipe/<int:id>/delete/', views.delete_recipe, name='delete_recipe'),
   path('ingredient/<int:id>/delete/', views.delete_ingredient, name='delete_ingredient'),
]
