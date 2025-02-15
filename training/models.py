from django.db import models

belt_choice = (
        ('B', 'Branca'),
        ('A', 'Azul'),
        ('R', 'Roxa'),
        ('M', 'Marron'),
        ('P', 'Preta')
    )

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_birth = models.DateField(null=True, blank=True)
    belt = models.CharField(max_length=1, choices=belt_choice, default='B')

    def __str__(self):
        return self.name
    
class CompletedClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    now_belt = models.CharField(max_length=2, choices=belt_choice, default='B')

    def __str__(self):
        return self.student.name
