from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    Roll = models.IntegerField(primary_key=True)
    adress = models.TextField()
    father_name = models.TextField(default='rahim')
    
    
    
    def __str__(self):
        return  f"{self.name} - {self.Roll} - {self.adress} - {self.father_name}"