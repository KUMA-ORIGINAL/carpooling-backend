from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение позволяет только чтение для всех,
    но только администраторы могут изменять объекты.
    """
    def has_permission(self, request, view):
        # Если запрос на безопасный метод (GET, HEAD, OPTIONS), разрешаем доступ
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для остальных методов требуется, чтобы пользователь был администратором
        return request.user and request.user.is_staff
