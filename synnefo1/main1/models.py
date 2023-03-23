from django.db import models
class Department(models.Model):

# Create your models here.
 dep_name=models.CharField(max_length=50)
 def __str__(self):
     return self.dep_name
 class Batch(models.Model):
    batch_time=models.CharField(max_length=50)
    def __str__(self):
       return self.batch_time
 class student(models.Model):
    std_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dept=models.ForeignKey(Department,default=1, on_delete=models.CASCADE)

