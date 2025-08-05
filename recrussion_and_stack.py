from random import randint


class RecreationAndStack:
    def __init__(self, n = None, lists = None, arr = None, num =  None):
        self.n = n
        self.lists = lists
        self.arr = arr
        self.num = num

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * r.factorial(n -1)

    def summ_list(self, lists):
        if len(lists) == 1:
            return lists[-1]
        else:
            last = lists.pop()
            return last + r.summ_list(lists)

    def binary_search(self, arr, num):
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

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0



r = RecreationAndStack()
print(f'>>> Factorial 5 = {r.factorial(n=5)}')

l = [5, 15, 34, 55, 30, 1, 8]
print(f'>>> Summ numbs list = {r.summ_list(lists=l)}')

a = []
for i in range(15):
    a.append(randint(0, 100))

#print(arr)
a.sort()
print(f'>>> Random list a  \n {a}')

number = 41
print(f'>>> Binary search num = {number} in list {r.binary_search(arr=a, num=number)}')


s = Stack()
s.push(15)
s.push(30)
print(s.pop())  # Вывод: 2
print(s.peek())  # Вывод: 1
