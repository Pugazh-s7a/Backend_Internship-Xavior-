from django.db import models

# Create your models here.
class Users(models.Model):
    urollno=models.CharField(primary_key=True,max_length=10)
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=100)
    ucontact =models.CharField(max_length=10)

    class Meta:
        db_table= "user"

class Mark(models.Model):
    users_uid=models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    subject1=models.CharField(max_length=100)
    score=models.CharField(max_length=10)

    class Meta:
        db_table="mark"

