from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.utils import timezone
from datetime import timedelta

# доступ только для владельца объекта
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated # пользователь должен быть авторизован
                and not request.user.is_staff # пользователь не должен быть админом
        )
# проверяем для конкретного объекта
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user # разрешаем доступ только владельцу

# права для анонимного пользователя
class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS # разрешаем только безопасные методы

# права для модератора
class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.is_staff
                and request.method in ("GET", "PUT", "PATCH", "DELETE")
        )

# редактирование в течение 15 мин после создания
class CanEditWithIn15Minutes(BasePermission):
    def has_object_permission(self, request, view, obj):
        time_passed = timezone.now() - obj.created_at # настоящее время - время создания объекта
        return time_passed <= timedelta(minutes=15) # разрешаем если результат меньше 15 мин