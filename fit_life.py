# Проект FitLife - MVP версия 1.0
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Создаем константы
WATER = 30
ML_TO_L = 1000

# Принимаем имя пользователя
name_user = input('Введите имя:')


# Принимаем возраст пользователя
user_age = int(input('Введите Ваш возраст:'))


# Принимаем вес пользователя
user_weight = float(input('Введите Ваш вес в кг.:'))


# Принимаем рост пользователя
user_height = float(input('Введите Ваш рост в метрах (пример 1.75):'))


# Рассчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)


# Рассчет кол-ва воды на вес
water_needed = round(user_weight * WATER / ML_TO_L, 1)


# Вывод красивого результата
print("=" * 50)
print(f'Отчет для пользователя: {name_user}, возраст {user_age}')
print(f'Твой индекс массы тела - {bmi}')
print(f'Необходимое потребление воды - {water_needed} л. в день')
print("Расчет окончен. Будьте здоровы")
