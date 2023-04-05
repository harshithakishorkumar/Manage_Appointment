from django.db import models

# Create your models here.

class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'AdminDetails'


class Doctor(models.Model):
	Name 		= models.CharField(max_length=100,default=None)
	username 	= models.CharField(max_length=100,default=None)
	password 	= models.CharField(max_length=100,default=None)
	Age 		= models.CharField(max_length=100,default=None)
	Gender 		= models.CharField(max_length=100,default=None)
	Phone 		= models.CharField(max_length=100,default=None)
	Address 	= models.CharField(max_length=100,default=None)
	Speciality 	= models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'Doctor'

class Patient_Details(models.Model):
	Name 		= models.CharField(max_length=100,default=None)
	Age 		= models.CharField(max_length=100,default=None)
	Gender 		= models.CharField(max_length=100,default=None)
	Phone 		= models.CharField(max_length=100,default=None)
	Address 	= models.CharField(max_length=100,default=None)
	Medication 	= models.CharField(max_length=100,default=None,null=True)
	Username 	= models.CharField(max_length=100,default=None)
	Password 	= models.CharField(max_length=100,default=None)
	class Meta:
		db_table='Patient_Details'

class Booking(models.Model):
	Doctor_Id = models.CharField(max_length=100,default=None)
	Patient_Id = models.CharField(max_length=100,default=None)
	Slot = models.CharField(max_length=100,default=None)
	Date = models.CharField(max_length=100,default=None)
	Treatment 	= models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'Booking'

class Feedback(models.Model):
	Patient_Id = models.CharField(max_length=100,default=None)
	Feedback = models.CharField(max_length=300,default=None)
	class Meta:
		db_table = "Feedback"
