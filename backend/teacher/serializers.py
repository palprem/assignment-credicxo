from rest_framework import serializers

from users.models import Users
from .models import Teacher

class TeacherAuthSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={"input_type":"password"},label="Confirm Password",required=True)
    
    class Meta:
        model = Users
        fields=["email", "password", "password_confirm"]
        extra_kwargs={"password":{"write_only":True},"password_confirm":{"write_only":True,}}

    def __init__(self,*args,**kwargs):
        super(TeacherAuthSerializer, self).__init__(*args,**kwargs)
        self.fields["password"].style={"input_type":"password"}

    def validate_password_confirm(self, data):
        password=self.get_initial().get("password")
        password_confirm=data

        if password != password_confirm:
            raise serializers.ValidationError("Passwords did not match.")
        return data

    def validate_email(self,value):
        email=value
        user_qs=Users.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("email already exists.")
        return value


class CreateTeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'