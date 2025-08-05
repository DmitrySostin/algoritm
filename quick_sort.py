import time
from random import randint

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return (time.time() - start) * 1_000_000

def meas_time(sort_func, num):
    start = time.time()
    sort_func(num)
    return (time.time() - start) * 1_000_000

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return  1
    else:
        #print(f'+Stek #{n:2.0f}  '*n)
        return fibonacci(n - 1) + fibonacci(n - 2)


def find_max(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])

    return max(left_max, right_max)

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


sizes = [10, 100, 1000]


print(f'Fibonacci time run: {meas_time(fibonacci, 10):20.2f} μs')

arr = []
for i in range(15):
    arr.append(randint(0, 50))

print(f'Max element in lens: {measure_time(find_max, arr):19.2f} μs')

for size in sizes:
    arr = []
    for i in range(size):
        arr.append(randint(0, 500))
    print(f'Time in Quick sort {size} elements {meas_time(quicksort, arr):9.2f} μs')