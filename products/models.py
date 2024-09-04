from django.db import models


class Supermarket(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.supermarket} - {self.price}"
