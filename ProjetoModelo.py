# backend/app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
"""
Descrição dos Modelos:

- User: Extende o modelo de usuário padrão do Django para utilizar o e-mail como campo de login único.
- Product: Representa os produtos cadastrados pelo empreendedor, incluindo detalhes como nome, descrição, preço e quantidade em estoque.
- Sale: Registra as vendas realizadas, atualiza automaticamente o estoque e calcula o preço total da venda.

"""
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        self.product.quantity_in_stock -= self.quantity
        self.product.save()
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} sold by {self.seller.username}"
