from django.core import mail
from django.test import TestCase, RequestFactory
import unittest
from rest_framework.reverse import reverse
# from django.urls import reverse
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from rest_framework.utils import json
from django.contrib.auth import authenticate
from django.conf import settings
from .views import ProductInfoView, CategoryView, ShopView, RegisterAccount, LoginAccount
from .models import User, Product, Category, ConfirmEmailToken
from django.test import Client
# Create your tests here.
from django.contrib import auth

class SimpleTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(first_name='sergey', last_name='suchkov', email='ser3421@rambler.ru',
                                                                            company='dsf', position='fdfs', password='Sergey1234', type='shop')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.type = 'shop'
        self.user.save()
        self.c = APIClient()
        # self.c.login(email='ser3421@rambler.ru', password='Sergey1234')
        log = self.c.post(reverse('backend:user-login'),
                           {'email':'ser3421@rambler.ru', 'password':'Sergey1234'})
        # self.assertEqual(log.json()['Token'], False)
        self.c.credentials(HTTP_AUTHORIZATION='Token ' + log.json()['Token'])
        self.c.post(reverse('backend:partner-update'), {'url': 'https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml'})
        # self.assertEqual(response.json(), 200)
    def test_products(self):
        response = self.c.get(reverse('backend:products'), {'shop_id':1, 'category_id':224})
        self.assertEqual(response.json()[0]['model'], 'apple/iphone/xs-max')
    def test_categories(self):
        # self.c = APIClient()
        response = self.c.get(reverse('backend:categories'))
        self.assertEqual(response.json()['results'][0]['id'], 224)

    def test_shops(self):
        response = self.c.get(reverse('backend:shops'))
        self.assertEqual(response.json()['results'][0]['name'], 'Связной')

    def test_basket_post(self):
        response = self.c.post(reverse('backend:basket'), {'items':'[{"product_info":1,"quantity":2}, {"product_info":2,"quantity":1}]'})
        self.assertEqual(response.json()['Status'], True)
    def test_basket_get(self):
        response = self.c.get(reverse('backend:basket'))
        self.assertEqual(response.status_code, 200)

    #     # self.factory = RequestFactory()
    #     request = self.factory.get('/api/v1/shops/')
    #     response = ShopView.as_view()(request)
    #     self.assertEqual(response.content, 200)


