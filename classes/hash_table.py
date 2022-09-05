import itertools
class HashTable:
    def __init__(self):
        self.size = 64 # sets default size to a fixed length
        self.map = [None] * self.size # where data is stored

    ''' 
    Calculates the index for the key
    '''
    def _get_hash(self, key):
        hash = 0

        for char in str(key):
            hash += ord(char)

        return hash % self.size

    '''
    Inserts an element into the hash O(1)
    '''
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # Key Doesn't exist? Insert new key/value pair
        if self.map[key_hash] is None:

            self.map[key_hash] = list([key_value])
            return True

        else: # Exists? Update
            for pair in self.map[key_hash]:

                if pair[0] == key:
                    pair[1] = value
                    return True

            self.map[key_hash].append(key_value)
            return True

    '''
    Returns key/value pair
    '''
    def lookup(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None

    '''
    Deletes a key/value pair O(1)
    '''
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

        return False


    '''
    Returns the keys of the hashmap
    '''
    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr


    def print(self):
        arr = []
        for item in self.map:
            if item is not None:
                arr.append(item)

        new_arr = list(itertools.chain.from_iterable(arr))

        for item in new_arr:
            item[1].print()



