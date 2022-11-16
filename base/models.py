from django.db import models

# Create your models here.

class Student(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField(max_length=60)
    email= models.EmailField(max_length = 254)
    phone=models.IntegerField()
    classes=models.IntegerField()
    marks=models.FloatField()
    
    def __str__(self):
        return self.student_name
    