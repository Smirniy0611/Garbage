def fast_sort(array):
    if len(array) < 2:
        return array
    else:
        reference = array[0]
        before = [i for i in array if i < reference]
        after = [i for i in array if i > reference]
        return fast_sort(before) + [reference] + fast_sort(after)

a = [1, 2, 9, 98, 51.5, -10]
print(fast_sort(a))
