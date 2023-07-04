while True:
    n = int(input('Введите число: '))
    if n == 0:
        exit()
    else:
        k = 0
        f = 1
        while k < n:
            k += 1
            f *= k
        print(f)

