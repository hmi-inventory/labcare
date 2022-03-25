from django.db import models

# Create your models here.
class ftp(models.Model):
	mac = models.CharField(max_length=500,default="")
	username = models.CharField(max_length=200, null=False)
	companyname = models.CharField(max_length=200,default="abc")
	security_key = models.CharField(max_length=200,null=False,unique=False)


class register(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	username = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	phone = models.IntegerField(null=True)
	address = models.TextField(max_length=500,null=True)

