from django.test import TestCase, RequestFactory
import unittest

from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from rest_framework.utils import json

from .views import ProductInfoView, CategoryView, ShopView, RegisterAccount, LoginAccount
from .models import User, Product, Category
from django.test import Client
# Create your tests here.
from django.contrib import auth

class SimpleTest(APITestCase):
    # def setUp(self):
        # Every test needs a client.
        # self.factory = RequestFactory()
        # self.c =Client()
        # self.user = User.objects.create(first_name='sergey', last_name='suchkov', email='ser3421@rambler.ru', company='dsf', position='fdfs', password='sergey1234', type='shop')
    def test_products(self):
        # self.factory = APIRequestFactory()
        self.c = APIClient()
    #
        a = self.c.get('/api/v1/products/')
        # response = ProductInfoView.as_view()(request)
        self.assertEqual(a, 200)
    # def test_categories(self):
    #     # self.factory = RequestFactory()
    #     request = self.factory.get('/api/v1/categories/')
    #     response = CategoryView.as_view()(request)
    #     response.render()
    #     a = json.loads(response.content)
    #     self.assertEqual(a['results'], 200)
    # def test_shops(self):
    #     # self.factory = RequestFactory()
    #     request = self.factory.get('/api/v1/shops/')
    #     response = ShopView.as_view()(request)
    #     self.assertEqual(response.content, 200)
    # def test_register(self):
    #     # self.factory = RequestFactory()
    #
    #     request = self.factory.post('/api/v1/user/register/', {'first_name': 'sergey', 'last_name': 'suchkov', 'email': 'ser3421@rambler.ru', 'company': 'dsf', 'position': 'fdfs', 'contacts': '234', 'type': 'shop'})
    #     response = RegisterAccount.as_view()(request)
    #     self.assertEqual(response.status_code, 200)
    # def test_login(self):
        # self.factory = RequestFactory()
        # client = APIClient()
        # response = client.post('/api/v1/user/login/',{'email':'ser3421@rambler.ru', 'password':'sergey1234'},format='json')
        # response = LoginAccount.as_view()(request)
        # self.assertEqual(response.data, 200)

