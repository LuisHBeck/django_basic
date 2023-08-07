from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=25)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Stock quantity')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    firts_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Costumers'


    def __str__(self) -> str:
        return f'{self.firts_name} {self.last_name}'