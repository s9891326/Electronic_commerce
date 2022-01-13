from django.test import TestCase
from django.urls import resolve

from shop.views import shop_view


class TestShopPageView(TestCase):
    def test_resolve_shop(self):
        found = resolve("/")
        self.assertEqual(found.func.__name__, shop_view.__name__)

    def test_reachable_shop(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_template_shop(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'shop/shop.html')

    def test_title_shop(self):
        response = self.client.get("/")
        self.assertContains(response, 'Verti')


