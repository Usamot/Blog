from django.db import models



class Blog(models.Model):
    # id = models.CharField(max_length=100, primary_key=True, )
    img = models.CharField(max_length=1000)
    title= models.CharField(max_length=1000)
    content=models.CharField(max_length=2000)
    author=models.CharField(max_length=200)

# Create your models here.
