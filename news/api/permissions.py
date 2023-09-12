from rest_framework import permissions


class IsAuthenticatedOrAdmin(permissions.BasePermission):

        def has_permission(self, request, view):
                if request.user.is_staff or request.method in permissions.SAFE_METHODS:
                        return True
                

