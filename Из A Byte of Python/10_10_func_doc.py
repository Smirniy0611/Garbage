def printMax(x, y):
    ''' Выводит максимальное из двух чисел.

Оба значения должны быть целыми числами '''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(8, 10)
print()
print(printMax.__doc__)
help(printMax)
