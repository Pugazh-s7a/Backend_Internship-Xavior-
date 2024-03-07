from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

class user_access(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    role = models.CharField(max_length=100)

