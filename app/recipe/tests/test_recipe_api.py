"""
Tests for recipe APIs.
"""

from decimal import Decimal
from typing_extensions import override
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Recipe
from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """Create and return a sample recipe."""
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdf',
    }
    defaults.update(params)
    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeAPITests(APITestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = self.client_class()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeAPITests(APITestCase):
    """Test authenticated API requests."""

    @override
    def setUp(self):
        self.client = self.client_class()
        self.user = get_user_model().objects.create_user('user@example.com', 'testpass123')
        self.client.force_authenticate(self.user)

    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes."""
        create_recipe(user=self.user, title='1st recipe')
        create_recipe(user=self.user, title='2nd recipe')
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        recipes = Recipe.objects.all().order_by('-id')
        serialized_recipes = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.data, serialized_recipes)

    def test_recipe_list_limited_to_user(self):
        """Test list of recipes is limited to authenticated user."""
        other_user = get_user_model().objects.create_user('other@example.com', 'pass123')
        create_recipe(user=other_user)
        create_recipe(user=self.user)
        res = self.client.get(RECIPES_URL)

        user_recipes = Recipe.objects.filter(user=self.user)
        serialized_recipes = RecipeSerializer(user_recipes)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized_recipes)
