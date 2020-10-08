from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url('creae-teacher/', views.CreateTeacherApiViews.as_view()),
    url('teacher-list/', views.ListOfTeacherApiViews.as_view()),
    # url('create-student/',views.CreateStudentApiViews.as_view())
]