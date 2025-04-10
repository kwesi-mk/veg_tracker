from rest_framework import permissions

class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'buyer'
    
class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'farmer'

class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'driver'

