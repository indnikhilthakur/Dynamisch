from rest_framework.permissions import BasePermission

class custom_get_permission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method == 'POST':
            return True
        return False