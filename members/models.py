from django.db import models

# Create your models here.


class Batch(models.Model):
   batch_name=models.CharField(max_length=100)
   batch_picture=models.CharField(max_length=100)
   def __str__(self):
      return self.batch_name

class BatchDetails(models.Model):
   batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
   name=models.CharField(max_length=100)
   position=models.CharField(max_length=400)
   dp=models.CharField(max_length=1000)
   def __str__(self):
      return self.name