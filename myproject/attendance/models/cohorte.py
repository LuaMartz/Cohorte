from django.db import models

class Cohorte(models.Model):
    name = models.CharField(max_length=50)
    group_director = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    number_students_initial = models.IntegerField(default=0)
    number = models.IntegerField(default=9)

    def __str__(self):
        return 'Nombre: ' + self.name + ' Número de cohorte: ' + str(self.number) + ' Director de grupo: ' + self.group_director + ' Curso: ' + self.course + ' Número de estudiantes Inicial: ' + str(self.number_students_initial) + ' Número de estudiantes: ' + str(self.number)