from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserLoginSerializer
# Create your views here.

class UserLoginApi(APIView):

    # permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        email,user_id = serializer.data['email'].split()
        # print(serializer.data)
        response = {
            'success' : True,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            'id':user_id,
            'email':email
        }
        return Response(response)