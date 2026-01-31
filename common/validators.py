from datetime import date
from product import serializers

# Проверка возраста
def age_validator(user):
        birthdate = user.birthdate
        if not birthdate:
            raise serializers.ValidationError("Укажите дату рождения, чтобы создать продукт.")
        age = (date.today() - birthdate).days // 365
        if age < 18:
            raise serializers.ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")