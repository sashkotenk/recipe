from django.urls import reverse
from django.test import TestCase
from .models import Category, Recipe

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(title='Category 1')
        self.cat2 = Category.objects.create(title='Category 2')
        # Create 15 recipes
        for i in range(15):
            category = self.cat1 if i % 2 == 0 else self.cat2
            Recipe.objects.create(title=f'Recipe {i}', category=category)

    def test_main_view_returns_10_or_fewer(self):
        url = reverse('recipe:main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        recipes = response.context['recipes']
        self.assertTrue(len(recipes) <= 10)
        for r in recipes:
            self.assertIsInstance(r, Recipe)

    def test_category_detail_shows_correct_recipes(self):
        url = reverse('recipe:category_detail', args=[self.cat1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_detail.html')
        self.assertEqual(list(response.context['recipes']), list(Recipe.objects.filter(category=self.cat1)))

