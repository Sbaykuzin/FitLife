# Проект FitLife - MVP версия 1.0
import io
import sys

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


WATER = 30
ML_TO_L = 1000


name_user = input('Введите имя:')


user_age = int(input('Введите Ваш возраст:'))


user_weight = float(input('Введите Ваш вес в кг.:'))


user_height = float(input('Введите Ваш рост в метрах (пример 1.75):'))


# Рассчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)


# Рассчет кол-ва воды на вес
water_needed = round(user_weight * WATER / ML_TO_L, 1)


print("=" * 50)
print(f'Отчет для пользователя: {name_user}, возраст {user_age}')
print(f'Твой индекс массы тела - {bmi}')
print(f'Необходимое потребление воды - {water_needed} л. в день')
print("Расчет окончен. Будьте здоровы")
