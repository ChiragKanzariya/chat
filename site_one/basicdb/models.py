from django.db import models

# Create your models here.
class UserData2(models.Model):
	name = models.CharField(max_length=50),
	state = models.CharField(max_length=50),
	city = models.CharField(max_length=50),
	contact = models.BigIntegerField(),
	password = models.CharField(max_length=50),
	key = models.IntegerField()