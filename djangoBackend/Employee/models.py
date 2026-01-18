from django.db import models
from django.core.validators import RegexValidator



#Modelo base que representa un empleado

class Employee(models.Model):
    
    class Deparment(models.TextChoices):
        IT = 'IT', 'Information Technology'
        HR = 'HR', 'Human Resources'
        FINANCE = 'FIN', 'Finance'
        OPERATION = 'OPS', 'Operations'

    name = models.CharField(max_length=255) #Nombre completo;
    birthday = models.DateField()
    position = models.CharField(max_length=100) #esto tambien puede ser su propio modelo
    deparment = models.CharField(max_length=5, choices=Deparment.choices)
    entry_date = models.DateField() #fecha de primer dia de trabajo
    creation_date = models.DateField(auto_now_add=True) #fecha de creacion del empleado
    is_active = models.BooleanField(default=True)

    dni = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{7,8}-[0-9kK]$',
                message='El RUT debe tener el formato 12345678-9'
            )
        ])

    def __str__(self):
        return f"{self.name}-{self.dni}"


class Log(models.Model):

    class Level(models.IntegerChoices):
        CRITICAL = 1, "Critical"
        MEDIUM = 2, "Medium"
        INFO = 3, "Informative"

    creation_date = models.DateField(auto_now_add=True) #fecha de creacion del empleado
    description = models.CharField(max_length=255)
    level = models.IntegerField(choices=Level.choices, default = Level.INFO)
