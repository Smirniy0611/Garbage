def kvadrat(a):
    """Принимает число и выдает его в квадрате"""
    print("Ваше число в квадрате: ", a ** 2)


kvadrat(5)


def kvadrat_2():
    a = int(input("Введите число:"))
    print(a ** 2)


kvadrat_2()


def len_2(a):
    a = str(a)
    n = 0
    for i in a:
        n += 1
    print(n)


x = "GHju v  cvk n cvm"
len_2(x)


def func_outer():
    x = 2
    print("x равно ", x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print("Локальное х сменилось на ", x)


func_outer()


def say(message, x = 2):
    print(message * x)


say("hallo", 5)
