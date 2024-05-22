class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    #returns the remainder of the key divided by the size of the table.
    def _hash(self, key):
        return key % self.size
    
    #inserts a key-value pair into the hash table. 
    #It computes the hash of the key and uses it as an index to store the value in the table.
    def set(self, key, value):
        hash_key = self._hash(key)
        self.table[hash_key] = value
    
    #retrieves the value associated with a given key
    def get(self, key):
        hash_key = self._hash(key)
        return self.table[hash_key]

# Usage
ht = HashTable()
ht.set(1, 'one')
ht.set(2, 'two')
print(ht.get(1))
print(ht.get(2))  