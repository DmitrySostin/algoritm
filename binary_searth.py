# В сравнении с линейным поиском и замер времени выполнения скрипта сильных различий нет

import timeit

def binary_arr(arr, num):
    first = 0
    mid = len(arr) // 2
    last = len(arr) - 1

    while arr[mid] != num and first <= last:
        if num > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2

    if first > last:
        return -1
    else:
        return mid


numb = int(input(">>> Enter number:\n<<< "))
s = """def err_def():
    arr_hundred = [11, 98, 351, 193, 238, 111, 263, 105, 367, 292, 74, 257, 67, 320, 344, 420, 89, 377, 293, 59, 325, 402,
                   39, 143, 358, 271, 30, 359, 73, 474, 116, 178, 482, 34, 476, 201, 490, 191, 101, 163, 159, 455, 236, 296,
                   206, 202, 21, 464, 218, 114, 118, 486, 344, 450, 71, 458, 257, 368, 98, 124, 164, 174, 266, 7, 203, 318,
                   43, 338, 278, 89, 69, 287, 8, 256, 460, 181, 125, 496, 452, 380, 326, 357, 137, 157, 14, 382, 116, 179,
                   131, 445, 220, 112, 388, 117, 10, 261, 285, 492, 298, 440, 451]
    arr_hundred.sort()
    print(f'>>> {binary_arr(arr, numb)}')"""

print(timeit.timeit(stmt=s, number=100))