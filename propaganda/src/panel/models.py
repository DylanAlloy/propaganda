from django.db import models

# Create your models here.
class Account(models.Model):
	user_name = models.CharField(max_length=20)
	password = models.CharField(max_length=18)
	secret = models.CharField(max_length=100)
	tag = models.CharField(max_length=20, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	user = models.ForeignKey('auth.User', null=True)
	is_active = models.BooleanField(default=False)

	def __str__(self): #Python 3.3 is __str__
		return str(self.user)
