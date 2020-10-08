from rest_framework.permissions import(
    IsAuthenticated, 
    AllowAny, 
    IsAdminUser
)

from rest_framework.views import APIView

from .serializers import (
    StudentAuthSerializer,
    CreateStudentProfileSerializer
)
from rest_framework.response import Response
from users.models import Users
from mysite.hash_permissions import IsTeacherAndSuperUser, IsStudentUser
from .models import Student


# Create your views here.

class CreateStudentApiViews(APIView):
    permission_classes = (IsTeacherAndSuperUser,)
    def post(self,request):

        data = request.data
        try:
            auth_student = {"email":data['email'],"password":data['password'],"password_confirm":data['password_confirm']}
            data.pop('password')
            data.pop('password_confirm')
        except Exception as e:
            return Response({"status":False,"msg":"Email, Password, Confirm Password fields are required"})

        serializer_class = StudentAuthSerializer(data=auth_student)
        if serializer_class.is_valid():
            student_auth = Users()
            student_auth.email = serializer_class.data['email']
            student_auth.is_student = True
            student_auth.set_password(serializer_class.data['password_confirm'])
            student_auth.save()
            print(student_auth.id,">>>>>>>>>>>..")
            data['id'] = student_auth.id
            student_serializer = CreateStudentProfileSerializer(data=data)

            if student_serializer.is_valid():
                student_serializer.save()
                return Response({"status":True,"msg":"Student created successfully!...","data":student_serializer.data})

            return Response({"status":False,"error": student_serializer.errors})

        return Response({"status":False,"error":serializer_class.errors})

class ListOfStudentApiViews(APIView):
    permission_classes = (IsTeacherAndSuperUser,)
    def get(self,request):
        data = Student.objects.all()
        serializer_class = CreateStudentProfileSerializer(data, many=True)
        return Response ({"status":True,"msg":"All student!..","data":serializer_class.data})

class StudentDetailsApiViews(APIView):
    permission_classes = (IsStudentUser,)
    def get(self,request):
        try:
            data = Student.objects.get(id=request.user.id)
            serializer_class = CreateStudentProfileSerializer(data)
            return Response ({"status":True,"msg":"Student details!..","data":serializer_class.data})
        except Exception as e:
            print(e)
            return Response ({"status":False,"msg":"Details not found.."})

# {
#     "email":"prem@gmail.com",
#     "password":"prem@123",
#     "password_confirm":"prem@123",
#     "full_name":"prem pal"
# }