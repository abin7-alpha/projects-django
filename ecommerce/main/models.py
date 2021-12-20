from django.db import models

# Create your models here.

class Sex(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, default=False, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, default=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=False, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, default=False, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to='pics', null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
