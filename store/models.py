from django.db import models

# Create your models here.


class Category(models.Model):
    nom = models.CharField(unique=True)


class Tag(models.Model):
    tag = models.CharField()


class Product(models.Model):

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='', blank=True, null=True)
    category = models.ManyToManyField(Category, on_delete=models.CASCADE, related_name='Product-category')
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE, related_name='Product-tag')
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=1)


class Order(models.Model):

    ORDER_STATUS = (
        ("Validated", "Validated"),
        ("Canceled", "Canceled"),
        ("Deleted", "Deleted")
    )

    owner = models.ForeignKey(on_delete=models.CASCADE, related_name='Order-owner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Ordered-products')
    quantity = models.IntegerField(default=1)
    order_statu = models.CharField(max_length=120, choices=ORDER_STATUS, related_name='Order-statu')
    date = models.DateField()


class Cart(models.Model):

    owner = models.ForeignKey(unique=True, on_delete=models.CASCADE, related_name='Cart-owner')
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Cart-product')
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField()
