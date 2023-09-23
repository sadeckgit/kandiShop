from django.db import models

# Create your models here.
USER_ROLES = (
    ("Client", "Client"),
    ("Merchant", "Merchant"),
    ("Administrator", "Administrator"),
)
ORDER_STATUS = (
    ("Validated", "Validated"),
    ("Canceled", "Canceled"),
    ("Deleted", "Deleted")
)

PAYMENT_METHOD = (
    ("Mobile money", "Mobile money"),
    ("Celtis cash", "Celtis cash"),
    ("Paypal", "Paypal")
)


class Users(models.Model):
    name = models.CharField(max_length=120)
    mail = models.EmailField()
    phone = models.IntegerField()
    role = models.CharField(choices=USER_ROLES)
    payment_methode = models.CharField(choices=PAYMENT_METHOD)


class Category(models.Model):
    nature = models.CharField(unique=True)


class Tag(models.Model):
    tags = models.CharField()


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=1)


class Order(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_statu = models.CharField(max_length=120, choices=ORDER_STATUS)


class Cart(models.Model):
    owner = models.ForeignKey(Users, unique=True,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
