from django.db import models

# Create your models here.
class Product(models.Model):
    
    def nameFile(instance,filename):
        return '/'.join('images',str(instance.name),filename)
    name=models.CharField(max_length=255)
    picture=models.ImageField(upload_to=nameFile,blank=True)
    description=models.CharField(max_length=100)
    price=models.IntegerField()


    def __str__(self):
        return self.name
