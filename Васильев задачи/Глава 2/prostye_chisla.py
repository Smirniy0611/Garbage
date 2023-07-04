n = int(input('введите число: '))
int = n // 2
k = 2
while k <= int:
    if n % k == 0:
        print('это число не являтся простым')
        break
    k += 1
else:
    print('Это простое число')
