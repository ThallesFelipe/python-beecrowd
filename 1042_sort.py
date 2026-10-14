a, b, c = map(int, input().split())

array = [a, b, c]
array_not_sorted = array.copy()


def bubble_sort(array: list[int]):
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

    return array


bubble_sort(array)

print(array[0])
print(array[1])
print(array[2])

print()

print(array_not_sorted[0])
print(array_not_sorted[1])
print(array_not_sorted[2])
