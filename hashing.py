class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        hash_key = self._hash(key)
        self.table[hash_key] = key

    def print_table(self):
        for i in range(self.size):
            print(i, end = " ")
            print(self.table[i])

# Usage
size = int(input("Enter the size of the hash table: "))
ht = HashTable(size)
elements = input("Enter the elements to be hashed, separated by space: ").split()
print("key value")
for element in elements:
    ht.insert(int(element))
ht.print_table()