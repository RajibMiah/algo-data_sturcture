class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self , key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX  

    def add(self , key , value):
        h = self.get_hash(key)
        self.arr[h]= value

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]   

if __name__ == '__main__':
    t = HashTable()
    t.add('march 6', 50)
    t.get('march 6')


