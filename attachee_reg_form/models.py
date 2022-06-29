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

    
class Issue(models.Model):
    date =models.DateField(null=False, default='2022-06-22')
    floor = models.CharField(max_length=255)
    issue =models.CharField(max_length=2550)
    Resolved = models.CharField(max_length=255)
    name  =models.CharField(max_length=2550)

    def __str__(self):
        return self.issue
    
    #JSON
    def get_data(self):
        return {
            'date':self.date,
            'floor': self.floor,
            'issue':self.issue,
            'resolved':self.Resolved,
            'name':self.name,

        }

class Code(models.Model):
    code = models.CharField(max_length=10)

