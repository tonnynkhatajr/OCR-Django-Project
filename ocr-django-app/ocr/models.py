from django.db import models

# Create your models here.
class RecInsert(models.Model):
    fname=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dateofentry=models.CharField(max_length=100)

class Meta:
    db_table="hts_register_tb"