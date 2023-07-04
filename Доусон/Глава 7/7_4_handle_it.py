# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input('Введите число: '))
except:
    print('Похоже, это не число')

# Обработка исключений определенного типа
try:
    num = float(input('Введите число: '))
except ValueError:
    print('Это не число')

# Обработка исключений нескольких разных типов
print()
for value in (None, 'Привет!'):
    try:
        print('Пытаюсь преобразовать в число: ', value, '-->', end=' ')
        print(float(value))
    except (TypeError, ValueError):
        print('Похоже, это не число!')

print()
for value in (None, 'Привет!', 4):
    try:
        print('Пытаюсь преобразовать в число: ', value, '-->', end=' ')
        print(float(value))
    except TypeError:
        print('Я умею преобразовывать только строки и числа!')
    except ValueError:
        print('Я умею преобразовывать только строки, составленные из цифр')

# Получение аргумента исключения
try:
    num = float(input('Введите число: '))
except ValueError as x:
    print('Это не число. Интерпритатор как бы говорит нам: ')
    print(x)

# try/except/else
try:
    num = float(input('Введите число: '))
except ValueError:
    print('Это не число')
else:
    print('Вы ввели число ', num)