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

def category_detail(request, id):
    """
    Показує всі рецепти певної категорії за її id.
    Шаблон: category_detail.html
    """
    category = get_object_or_404(Category, id=id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipe/templates/category_detail.html', {
        'category': category,
        'recipes': recipes,
    })
