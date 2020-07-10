from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.product_name


class Photos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.short_description


class Videos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.short_description
