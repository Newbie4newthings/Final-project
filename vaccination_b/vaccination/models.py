from django.db import models

# Individual model
class Individual(models.Model):
    individual_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Admin model (for simplicity)
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    role = models.CharField(max_length=50, default='admin')
