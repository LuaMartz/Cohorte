from django.urls import path
from .views import students

from .views import views

urlpatterns = [
    path('', views.index, name = "index")
]

urlpatterns += [
    path("students", students.StudentListView.as_view(), name="students"),
    path("students/<int:pk>", students.StudentDetailView.as_view(), name="student_detail"),
    path("students/create", students.StudentCreateView.as_view(), name="student_create"),
]
