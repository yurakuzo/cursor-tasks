from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Customer').exists()


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Seller').exists()
