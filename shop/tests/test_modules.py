from django.db import models
from django.test import TestCase

# Create your tests here.
from shop.models import Product


class TestProductFieldType(TestCase):
    def test_name_field_type(self):
        self.assert_same_type("name", models.CharField)

    def test_price_field_type(self):
        self.assert_same_type("price", models.DecimalField)

    def test_img_field_type(self):
        self.assert_same_type("img", models.ImageField)

    def test_on_sale_field_type(self):
        self.assert_same_type("on_sale", models.BooleanField)

    def test_tag_field_type(self):
        self.assert_same_type("tag", models.CharField)

    def test_percent_off_field_type(self):
        self.assert_same_type("percent_off", models.DecimalField)

    def test_sale_price_field_type(self):
        self.assert_same_type("sale_price", models.DecimalField)

    def test_bought_counter_field_type(self):
        self.assert_same_type("bought_counter", models.DecimalField)

    def test_created_date_field_type(self):
        self.assert_same_type("created_date", models.DateTimeField)

    def test_published_date_field_type(self):
        self.assert_same_type("published_date", models.DateTimeField)

    def assert_same_type(self, field_name, field_type):
        self.assertTrue(isinstance(get_product_field(field_name), field_type))


def get_product_field(field_name):
    return Product._meta.get_field(field_name)
