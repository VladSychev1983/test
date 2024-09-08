from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        # разрешаем делать запросы на чтение всем.
        if request.method == 'GET':
            return True
        return request.user == obj.user
    