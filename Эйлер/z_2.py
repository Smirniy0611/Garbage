fib1 = fib2 = 1
for i in range(10):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2)
