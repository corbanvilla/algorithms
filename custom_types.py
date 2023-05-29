class Infinity:
    def __lt__(self, other):
        if (isinstance(other, Infinity)):
            raise TypeError("Cannot compare two infinities!")
        
        return False
    def __gt__(self, other):
        if (isinstance(other, Infinity)):
            raise TypeError("Cannot compare two infinities!")
        
        return True
    
    @staticmethod
    def isInfinity(obj1):
        return isinstance(obj1, Infinity)