a = [1, 2, 9, 98, 51.5, -10]


def summa(lists):
    if not lists:
        return 0
    return lists[0] + summa(lists[1:])


print(summa(a))


def quantity(lists):
    if not lists:
        return 0
    return 1 + quantity(lists[1:])


print(quantity(a))



