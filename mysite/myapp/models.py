from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
	users = User
	message = models.TextField() 


def _str_(self):
	return self.users.username

	
