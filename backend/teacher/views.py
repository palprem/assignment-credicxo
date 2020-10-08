from rest_framework.permissions import(
    IsAuthenticated, 
    AllowAny, 
    IsAdminUser
)

from rest_framework.views import APIView

from .serializers import (
    TeacherAuthSerializer,
    CreateTeacherProfileSerializer
)
from rest_framework.response import Response
from users.models import Users
from mysite.hash_permissions import IsTeacherUser
from .models import Teacher


# Create your views here.

class CreateTeacherApiViews(APIView):

    def post(self,request):

        data = request.data
        try:
            auth_vender = {"email":data['email'],"password":data['password'],"password_confirm":data['password_confirm']}
            data.pop('password')
            data.pop('password_confirm')
        except Exception as e:
            return Response({"status":False,"msg":"Email, Password, Confirm Password fields are required"})

        serializer_class = TeacherAuthSerializer(data=auth_vender)
        if serializer_class.is_valid():
            teacher_auth = Users()
            teacher_auth.email = serializer_class.data['email']
            teacher_auth.is_teacher = True
            teacher_auth.set_password(serializer_class.data['password_confirm'])
            teacher_auth.save()
            print(teacher_auth.id,">>>>>>>>>>>..")
            data['id'] = teacher_auth.id
            teacher_serializer = CreateTeacherProfileSerializer(data=data)

            if teacher_serializer.is_valid():
                teacher_serializer.save()
                return Response({"status":True,"msg":"Teacher created successfully!...","data":teacher_serializer.data})

            return Response({"status":False,"error": teacher_serializer.errors})

        return Response({"status":False,"error":serializer_class.errors})

class ListOfTeacherApiViews(APIView):
    permission_classes = (IsTeacherUser,)
    def get(self,request):
        data = Teacher.objects.all()
        serializer_class = CreateTeacherProfileSerializer(data, many=True)
        return Response ({"status":True,"msg":"All customer!..","data":serializer_class.data})

# {
#     "email":"prem@gmail.com",
#     "password":"prem@123",
#     "password_confirm":"prem@123",
#     "full_name":"prem pal"
# }