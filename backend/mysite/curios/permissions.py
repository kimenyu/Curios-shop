from rest_framework import permissions

class IsAdminUserorReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
    

class IsMerchantUser(permissions.BasePermission):
    """
    Custom permission to only allow merchants to perform certain actions.
    """

    def has_permission(self, request, view):
        # Check if the user making the request is authenticated
        if request.user.is_authenticated:
            # Check if the user is a merchant
            return request.user.is_merchant
        return False
