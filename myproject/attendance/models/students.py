from django.db import models
from django.urls import reverse
from .cohorte import Cohorte

class Student(models.Model):
    name = models.CharField(max_length=50)
    DOCUMENT_TYPE_CHOICE = (
        ("CC","Cédula Ciudadanía"),
        ("PPT", "Permiso Protección Temporal"),
        ("CE", "Cédula Extranjería"),
        ("TI","Tarjeta Identidad")
    )
    document_type = models.CharField(max_length=3,choices = DOCUMENT_TYPE_CHOICE, default ="CC")
    document_number = models.IntegerField(default=0)
    cohorte = models.ForeignKey(Cohorte, null= True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return 'Nombre: ' + self.name + ' Tipo de Documento: ' + self.document_type + ' Número de Documento: ' + str(self.document_number) + ' Cohorte: ' + str(self.cohorte)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])