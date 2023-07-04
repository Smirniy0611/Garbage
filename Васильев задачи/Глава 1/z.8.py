n = int(input('Введите количество символов: '))
f = []
f1 = 1
f2 = 0
while len(f) < n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    f.append(fn)
print(f)
