from django.shortcuts import render

# Create your views here.
from ..models.cohorte import Cohorte
from ..models.students import Student

def index(request):
    """Function to home site"""
    cohortes = Cohorte.objects.all()
    students = Student.objects.all()
    return render(
        request,
        'attendance/index.html',
        context =
        {
            "cohortes":cohortes,
            "students":students
        }
    )