from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Form(models.Model):
    first_name=models.CharField(max_length=255)
    second_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, default="mail")
    contact=models.BigIntegerField(null=False, default='070000000')
    university =models.CharField(max_length=255, default='university')
    start_date=models.DateField(null=False, default='2022-01-01')
    end_date=models.DateField(null=False, default='2022-03-30')
    supervisor=models.CharField(max_length=255, default='supervisor')
    department =models.CharField(null=False, default="department", max_length=255)


    def __str__(self):
        return self.first_name

    
