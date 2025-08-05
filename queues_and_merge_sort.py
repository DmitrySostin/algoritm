import time
from os import times
from random import randint


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        return self.items.append(items)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return -1

    def size(self):
        return len(self.items)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0# Слияние двух половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return (time.time() - start) * 1_000_000


################################################################################
tasks =["07.30 - Wake up",
    "07.35 - Drink tea with milk",
    "07.40 - Wash up",
    "07.50 - Go to work",
    "11.45 - Lunch",
    "12.50 - Work again",
    "17.00 - Time to go home",
    "19.00 - Do homework",
    "22.30 - Take a shower",
    "23.55 - Go to bed",
]

queue = Queue()

for task in tasks:
    queue.enqueue(task)

if not queue.is_empty():
    print(f">>> You have :{queue.size()+1} Task to day")

    for i in range(queue.size()):
        print(f'... {i+1:2.0f}  {queue.peek()}')
        queue.dequeue()

arr =  []
numbs = [10, 100, 1000]
for numb in numbs:
    arr.append(randint(0, 1000))
    tims = measure_time(merge_sort, arr)
    print(f'>>> Time work mega_sort in {numb:6.0f} - lens {tims:7.2f} μs, one operation = {tims / numb : 4.3f}')

print("[INFO] the more values, the less is required to complete 1 operation")