import random


def ask_number(question, low, high):
    """Просит ввести число из диапозона"""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except(TypeError, ValueError):
            print('Похоже, это не число(((. Попробуйте еще раз, плиз! ')
    return response


def main():
    the_number = random.randint(1, 100)
    guess = ask_number('Введите ваше предположение: ', 0, 100)
    tries = 1
    while guess != the_number:
        if guess > the_number:
            print('меньше')
        else:
            print('больше')
        guess = ask_number('Введите ваше предположение: ', 0, 100)
        tries += 1
    print('Вам удалось отгадать число. Вы затратили ', tries, 'попыток')


main()
