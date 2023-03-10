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

     




