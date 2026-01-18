from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nameProduct = models.CharField(max_length=255)
    quantity = models.IntegerField()
    productPhoto = models.ImageField()

    imageUpload = models.ImageField.storage()
    