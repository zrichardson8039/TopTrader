from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return request.method in SAFE_METHODS