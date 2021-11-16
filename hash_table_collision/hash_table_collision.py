
class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self , key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX  

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            print("element",element)
            if element[0] == key:
                return element[1]

    def __setitem__(self , key , value):
        h = self.get_hash(key)
        found = False
        for idx , element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key , value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
    

    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for index ,  element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                found = True
                break
        if not found :
            self.arr[h] = []        

if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 50
    t["march 50"] = 55
    t["march 10"] = 5
    t["march 17"] = 6
    print(t.arr)
    del t['march 50']
    print(t.arr)
    print(t["march 17"])
    


