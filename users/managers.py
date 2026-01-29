from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
    # Проверка email
        if not email:
            raise ValueError("Email is not found")
        email = self.normalize_email(email) # Встроенная проверка на корректность email
        user = self.model(email=email, **extra_fields) # Создание пользователя
        user.set_password(password) # Установка пароля (нельзя писать user.password = password)
        user.save() # Сохраняем
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        # Проверка телефона
        if not extra_fields.get("phone_number"):
            raise ValueError("Superuser must have phone_number")

        # Включаем все права по дефолту
        extra_fields.setdefault("is_superuser", True) # Полный доступ
        extra_fields.setdefault("is_staff", True) # Доступ в админку
        extra_fields.setdefault("is_active", True) # Аккаунт активен

        # Проверка, если вдруг что-то выключено
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")
        
        return self.create_user(email, password, **extra_fields) # Создаём супер пользователя