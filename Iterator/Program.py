#The algorithm iterates between 0 and an integer value passed as a parameter
class MyIterator():
    def __iter__(self):
        self.myAttr = 0
        return self
    def __next__(self):
        if self.myAttr <= self.number:
            n=self.myAttr
            self.myAttr+=1
            return n
        else:
            raise StopIteration
    @property
    def number(self):
        return self.__number__
    @number.setter
    def number(self,number):
        self.__number__ = number

m = MyIterator()
m.number=300
myIter = iter(m)
for x in myIter:
    print(x)