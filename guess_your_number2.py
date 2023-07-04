left = 1
right = 100
while True:
    current = (left+right)//2
    is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
    if is_right.lower() == 'да':
        print('Я его угадал!')
        break
    elif is_right=='больше':
        left = current + 1
    else:
        right = current - 1
