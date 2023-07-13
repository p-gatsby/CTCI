# Hashtables or Hashmap is a type of data structure that maps keys to its value pairs

class HashTable:
    
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range (0, self.size)]

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    
    def set(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]

        for i, kv in enumerate(slot):
            k, v = kv

            if key == k:
                key_exists = True
                break
        
        if key_exists:
            slot[i] = (key, value)
        else:
            slot.append((key, value))
    
    def get(self, key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]

        for kv in slot: 
            k, v =  kv
            
            if key == k:
                return v
            else: 
                raise KeyError('Does not exist.')
            
    def __setitem__(self, key, value):
        return self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    

    def __str__(self):
        return str(self.hashmap)

H = HashTable()

H['key1'] = 'value1'
H['key2'] = 'value2'
H['key3'] = 'value3'

print(H)

print(H['key1'])