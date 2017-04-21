from django.db import models

# Create your models here.
class ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rider_num = models.IntegerField()
