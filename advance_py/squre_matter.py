
class Squre:

    def __init__(self , side) -> None:
        self._side = side

    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self , value):
        if value >= 0:
            self._side = value
        else:
            print('error occured')    
    @property
    def area(self):
        return self._side ** 2

    @classmethod 
    def unit_square(cls):
        return cls(1)



if __name__ == '__main__':
    s = Squre(5)
    print(s.side)
    print(s.area)