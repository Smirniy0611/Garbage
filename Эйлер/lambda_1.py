def func(a, b):
    perim = lambda a, b: (a + b) * 2
    area = lambda a, b: a * b
    print(area(a, b), perim(a, b))


x = int(input())
y = int(input())
func(x, y)
