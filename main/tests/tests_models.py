from django.test import TestCase

from ..models import *

class CategoryModelTest(TestCase):
    
    def setUp(self):
        self.data = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.data.get_absolute_url(), '/category/test-category/')

    def test__str__(self):
        self.assertEqual(str(self.data), 'Test Category')


class ProductModelTest(TestCase):

    def setUp(self):
        self.data_category = Category.objects.create(
            name='Test Category',
            slug='test-category',
        )

        self.data_product = Product.objects.create(
            name='Product Test',
            description = 'description',
            price=1234,
            category_id = 1,
            slug='product',
        )
        
    def test_get_absolute_url(self):
        self.assertEqual(self.data_product.get_absolute_url(), '/product/product/')

    def test__str__(self):
        self.assertEqual(str(self.data_product), 'Product Test')
     




