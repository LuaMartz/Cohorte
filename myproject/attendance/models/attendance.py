from django.db import models
from .students import Student

class Attendance(models.Model):
    status = models.BooleanField(default=False)
    excusse = models.BooleanField(default=False)
    excusse_support = models.CharField(max_length=50)
    date = models.DateField(auto_now=000000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Estudiante: ' + str(self.student) + 'Estado: ' + str(self.status) + ' Excusas: ' + str(self.excusse) + ' Soporte de excusas: ' + self.excusse_support + ' Fecha: ' + str(self.date)