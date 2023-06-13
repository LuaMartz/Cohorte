from django.contrib import admin

# Register your models here.

from .models.cohorte import Cohorte
from .models.students import Student
from .models.attendance import Attendance

admin.site.register(Cohorte)
admin.site.register(Student)
admin.site.register(Attendance)

# Define new admin class
# class StudentAdmin(admin.ModelAdmin):
#     pass

# class CohorteAdmin(admin.ModelAdmin):

#     # Register the admin class with the associated model
#     admin.site.register(Student, StudentAdmin)
#     admin.site.register(Cohorte, CohorteAdmin)