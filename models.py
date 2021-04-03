from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)
    describe = models.TextField()
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=300)
    carNumber=models.CharField(max_length=200,null=False,unique=True)
    CIN=models.CharField(max_length=8)
    phone= models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)