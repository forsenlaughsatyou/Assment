
from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phoneNO = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photos')


class WorkExperience(models.Model):
    owner = models.ForeignKey(Employees, related_name='workexperience' ,on_delete=models.CASCADE) 
    companyName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=100)
    toDate = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Qualifications(models.Model):
    owner = models.ForeignKey(Employees, related_name='qualifications' ,on_delete=models.CASCADE)
    qualificationName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=100)
    toDate = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=2,decimal_places=2)

class Projects(models.Model):
    owner = models.ForeignKey(Employees, related_name='projects' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class addressDetails(models.Model):
    owner = models.ForeignKey(Employees, related_name='addressdetails',on_delete=models.CASCADE)
    Hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    