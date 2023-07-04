f1 = 1
f2 = 1
for i in range(10):
    f1, f2 = f2, f1 + f2
    print(f2)
