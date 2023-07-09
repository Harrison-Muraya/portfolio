from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.username
  
