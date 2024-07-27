from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        return self.base_price

class SeasonalProduct(Product):
    season_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def get_price(self):
        discount_amount = self.base_price * (self.season_discount / 100)
        return self.base_price - discount_amount

class BulkProduct(Product):
    bulk_quantity = models.PositiveIntegerField()
    bulk_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def get_bulk_price(self, quantity):
        if quantity >= self.bulk_quantity:
            discount_amount = self.base_price * (self.bulk_discount / 100)
            return self.base_price - discount_amount
        return self.base_price

class Discount(models.Model):
    DISCOUNT_TYPE_CHOICES = (
        ('percentage', 'Percentage Discount'),
        ('fixed', 'Fixed Amount Discount'),
    )
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        if self.discount_type == 'percentage':
            discount_amount = price * (self.value / 100)
            return price - discount_amount
        elif self.discount_type == 'fixed':
            return max(price - self.value, 0)
        return price

class Order(models.Model):
    def get_total_price(self):
        total_price = 0
        for item in self.orderitem_set.all():
            product = item.product
            quantity = item.quantity
            discount = item.discount

            if isinstance(product, BulkProduct):
                price = product.get_bulk_price(quantity) * quantity
            else:
                price = product.get_price() * quantity

            if discount:
                price = discount.apply_discount(price)

            total_price += price
        
        return float(total_price)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)

