from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

def recipe_list(request):
   recipes = Recipe.objects.all()
   return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
   recipe = get_object_or_404(Recipe, id=id)
   ingredients = recipe.ingredients.all()
   ingredient_form = IngredientForm()

   if request.method == 'POST':
      ingredient_form = IngredientForm(request.POST)
      if ingredient_form.is_valid():
         ingredient = ingredient_form.save(commit=False)
         ingredient.recipe = recipe
         ingredient.save()
         return redirect('recipe_detail', id=recipe.id)

   return render(request, 'recipes/recipe_detail.html', {
      'recipe': recipe,
      'ingredients': ingredients,
      'ingredient_form': ingredient_form,
   })

def create_recipe(request):
   if request.method == 'POST':
      form = RecipeForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('recipe_list')
   else:
      form = RecipeForm()

   return render(request, 'recipes/create_recipe.html', {'form': form})

def delete_recipe(request, id):
   recipe = get_object_or_404(Recipe, id=id)
   recipe.delete()
   return redirect('recipe_list')

def delete_ingredient(request, id):
   ingredient = get_object_or_404(Ingredient, id=id)
   recipe_id = ingredient.recipe.id
   ingredient.delete()
   return redirect('recipe_detail', id=recipe_id)
