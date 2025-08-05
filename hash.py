class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delite(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return True
        return False

    def resaze(self):
        new_size = self.size * 2
        new_table = [None] * new_size

        old_table = self.table
        self.table = new_table
        self.size = new_size
        self.count = 0

        for bucket in old_table:
            if bucket is not None:
                for key, value in bucket:
                    self.insert(key, value)


def simple_string_hash(intput_string:str=None):
    hash_value = 0
    print(f'>>> +---------------+---------------+')
    print(f'>>> |  Symbol       |  ASCII-code   |')
    print(f'>>> +---------------+---------------+')
    for char in intput_string:
        print(f'>>> |       {char}       |       {ord(char):3.0f}     |')
        print(f'>>> +---------------+---------------+')
        hash_value += ord(char)

    return hash_value

def add_string_hash(input_string:str, input_hash:int):
    table.insert(input_string, input_hash)


table = HashTable(5)

print(f'>>> First size table: {table.size}')

print(f'>>> Add data in table.....')
for i in range(15):
    table.insert(f'key-{i}', f'value-{i}')
    print(f'>>> Add element {i}. Table size :{table.size}')

for i in range(table.size):
    if table.table[i] is not None:
        print(f'.... TABLE | INDEX : {i:3.0f} | {table.table[i]} |')

table.resaze()

for i in range(table.size):
    if table.table[i] is not None:
        print(f'.... TABLE | INDEX : {i:3.0f} | {table.table[i]} |')

print('#'*30)

input_data ="Remember about time!"
print(f'>>> Hash string "{input_data}" = {simple_string_hash(intput_string=input_data)}')


lorem_ipsum = [
    'Lorem ipsum dolor sit amet',
    'consectetur adipiscing elit',
    'Nam ac faucibus est',
    'Aenean dapibus urna ante',
    'ut sollicitudin mauris tincidunt et',
    'Fusce sed erat elementum',
    'posuere enim sed',
    'eleifend nunc',
    'Pellentesque lacinia risus in enim bibendum gravida.']

for lorem in lorem_ipsum:
    add_string_hash(input_string=lorem, input_hash=simple_string_hash(intput_string=lorem))

for i in range(table.size):
    if table.table[i] is not None:
        print(f'.... TABLE | INDEX : {i:3.0f} | {table.table[i]} |')


