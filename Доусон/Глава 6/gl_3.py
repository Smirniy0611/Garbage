print('Я загадаю число от 1 до 100, попробуй его отгадать')
print('Если загаданное число меньше твоего варианта, я напишу "Меньше"')
print('Если больше, я напишу "Больше"')

import random

tries = 0
attempt = None
x = random.randint(0, 100)
while attempt != x:
    attempt = int(input('Твоя версия?  '))
    if attempt > x:
        print('Загаданное число меньше, попробуй еще раз')
        tries += 1
    else:
        print('Загаданное число больше, попробуй еще раз')
        tries += 1
print('Да, верно, это число ', x, 'ты затратил ', tries, 'попыток')
