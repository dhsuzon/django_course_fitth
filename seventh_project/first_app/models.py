from django.db import models

class StudentModel(models.Model):
     Roll = models.IntegerField( primary_key=True)
     Name = models.CharField( max_length=20)
     Father_Name = models.CharField( max_length=20)
     Adress = models.TextField()
  
     def __str__(self):
          return f" Name:- {self.Name} - Roll: - {self.Roll} -Adress: - {self.Adress}"


     
