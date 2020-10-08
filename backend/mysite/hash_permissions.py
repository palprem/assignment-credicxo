from rest_framework import permissions

class IsTeacherUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user and (request.user.is_teacher or request.user.is_superuser))
        except Exception as e:
            return False
        


class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user and request.user.is_student)
        except Exception as e:
            return False