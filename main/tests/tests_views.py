from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

import datetime

from main.models import Category, Product, Review



class TestMainApplicationViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='password',
            email='user1@email.com'
        )

        self.user2 = User.objects.create_user(
            username='user2',
            password='password',
            email='user2@email.com'
        )

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

        self.product2 = Product.objects.create(
            name='product2',
            description='description2',
            price='200',
            category=self.category,
            slug='product2',
        )

        '''
        Первый продукт, средний рейтинг - 4,
        соотвественно, он должен быть первым.
        '''

        self.review1 = Review.objects.create(
            review='Good',
            user=self.user1,
            product=self.product1,
            created_at=datetime.datetime.today(),
            updated_at=datetime.datetime.today(),
            rating = 5
        )

        self.review2 = Review.objects.create(
            review='Not Good',
            user=self.user2,
            product=self.product1,
            created_at=datetime.datetime.today(),
            updated_at=datetime.datetime.today(),
            rating = 3
        )

        '''
        Второй продукт, средний рейтинг - 1
        соотвественно, он должен быть вторым.
        '''

        self.review3 = Review.objects.create(
            review='Bad',
            user=self.user1,
            product=self.product2,
            created_at=datetime.datetime.today(),
            updated_at=datetime.datetime.today(),
            rating = 1
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        products = response.context['object_list']
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'product1')
        self.assertContains(response, 'product2')
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0], self.product1)
        self.assertEqual(products[1], self.product2)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', kwargs={'slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)
        




