from django.db import models

# Create your models here.
class UserData(models.Model):
	name = models.CharField(max_length=20)
	username = models.CharField(max_length=20,default='',unique=True)
	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20)
	gender = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	pincode = models.IntegerField()
	email=models.CharField(max_length=20)
	dob = models.DateField()
	contact = models.BigIntegerField()
	password = models.CharField(max_length=20,default='')

class Chat(models.Model): 
	uid = models.IntegerField()
	chat = models.CharField(max_length=5000)
	