from  rest_framework.permissions import BasePermission , SAFE_METHODS

from django.conf import settings

class IsVendor(BasePermission):
    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.role == settings.ROLE_CHOICES['vendor']
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user