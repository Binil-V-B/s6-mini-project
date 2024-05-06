from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    vehicle_reg_no=models.CharField(max_length=10)
    login_time=models.DateTimeField("last seen")