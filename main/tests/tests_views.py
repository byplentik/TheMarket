from django.test import TestCase
from django.urls import reverse
from ..models import Category, Product

class CategoryDetailViewTestCase(TestCase):
    def setUp(self):
        self.data_category = Category.objects.create(
            name='Test Category',
            slug='test-category',
        )

        self.data_product1 = Product.objects.create(
            name='Test Product',
            description = 'description',
            price=1234,
            category_id = 1,
            slug='product',
        )

        self.data_product2 = Product.objects.create(
            name='Test Product2',
            description = 'description2',
            price=12342,
            category_id = 1,
            slug='product2',
        )

    def test_get_context_data(self):
        response = self.client.get(reverse('category_detail', kwargs={'slug': 'test-category'}))

        self.assertEqual(response.context['category'].name, 'Test Category')
        self.assertEqual(len(response.context['products']), 2)
        self.assertEqual(response.context['products'][0].name, 'Test Product')
        self.assertEqual(response.context['products'][1].name, 'Test Product2')
