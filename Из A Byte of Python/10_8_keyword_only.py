def total(initial=5, *numbers, extra_numbers):
    count = initial
    for number in numbers:
        count += number
    count += extra_numbers
    print(count)
total(10, 1, 2, 3, extra_numbers=50)
total(10, 1, 2, 3)