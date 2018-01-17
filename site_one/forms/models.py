from django.db import models

# Create your models here.
class RegisterForm(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)