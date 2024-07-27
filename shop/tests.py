from django.test import TestCase
from .models import Product, SeasonalProduct, BulkProduct, Discount, Order, OrderItem

class ProductTests(TestCase):

    def test_product_price(self):
        product = Product.objects.create(name="Regular Product", base_price=100)
        self.assertEqual(product.get_price(), 100)

    def test_seasonal_product_price(self):
        seasonal_product = SeasonalProduct.objects.create(name="Winter Coat", base_price=100, season_discount=20)
        self.assertEqual(seasonal_product.get_price(), 80)

    def test_bulk_product_price(self):
        bulk_product = BulkProduct.objects.create(name="Socks", base_price=5, bulk_quantity=10, bulk_discount=15)
        self.assertEqual(bulk_product.get_bulk_price(12), 4.25)
        self.assertEqual(bulk_product.get_bulk_price(8), 5)

class DiscountTests(TestCase):

    def test_percentage_discount(self):
        discount = Discount.objects.create(discount_type='percentage', value=10)
        self.assertEqual(discount.apply_discount(100), 90)

    def test_fixed_amount_discount(self):
        discount = Discount.objects.create(discount_type='fixed', value=30)
        self.assertEqual(discount.apply_discount(100), 70)
        self.assertEqual(discount.apply_discount(25), 0)




