from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category  # або як у вас називаються моделі

def main(request):
    """
    Головна сторінка: при кожному оновленні — 10 випадкових рецептів.
    """
    # Використовуємо order_by('?') для рандомного сортування
    recipes = Recipe.objects.order_by('?')[:10]
    return render(request, 'recipe/templates/main.html', {
        'recipes': recipes,
    })
