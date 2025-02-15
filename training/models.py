from django.db import models

class Student(models.Model):
    belt_choice = (
        ('B', 'Branca'),
        ('A', 'Azul'),
        ('R', 'Roxa'),
        ('M', 'Marron'),
        ('P', 'Preta')
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_birth = models.DateField(null=True, blank=True)
    belt = models.CharField(max_length=1, choices=belt_choice, default='B')

    def __str__(self):
        return self.name
