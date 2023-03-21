from rest_framework import permissions


class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            obj.user == request.user or request.user.is_staff)
