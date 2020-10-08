from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url('create-student/', views.CreateStudentApiViews.as_view()),
    url('list-student/',views.ListOfStudentApiViews.as_view()),
    url('student-details',views.StudentDetailsApiViews.as_view())
]