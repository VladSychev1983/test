from rest_framework import permissions
from rest_framework.exceptions import ValidationError

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.method == "DELETE" and obj.creator != request.user:
            raise ValidationError('Вы не можете удалять чужие объявления!')

        # Instance must have an attribute named `owner`.
        return obj.creator == request.user