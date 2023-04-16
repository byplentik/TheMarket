from django.test import TestCase

from accs.models import User

import datetime

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
        self.category = Category.objects.create(
            name='category',
            slug='category',
        )

        self.product1 = Product.objects.create(
            name='product1',
            description='description1',
            price='500',
            category=self.category,
            slug='product1',
        )

    def test_return_name_product(self):
        self.assertEqual(str(self.product1), 'product1')
        

class ReviewModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='category',
            slug='category',
        )

        self.product1 = Product.objects.create(
            name='product1',
            description='description1',
            price='500',
            category=self.category,
            slug='product1',
        )

        self.user1 = User.objects.create_user(
            username='user1',
            password='password',
            email='user1@email.com'
        )

        self.review1 = Review.objects.create(
            review='Good',
            user=self.user1,
            product=self.product1,
            created_at=datetime.datetime.today(),
            updated_at=datetime.datetime.today(),
            rating = 5
        )

    def test_return_name_product(self):
        self.assertEqual(str(self.review1), 'user1 : Good')
            




