from django.db import models
from django.utils import timezone

class Users(models.Model):
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    contact = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname, self.lastname, self.email, self.contact,self.time
  
