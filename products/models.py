from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    prince = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    
