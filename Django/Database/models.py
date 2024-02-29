from django.db import models

# Create your models here.


from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100,null= True)
    email = models.CharField(max_length=100,null= True)
    description = models.TextField()