import math
#THIS IS A SMALL EDUCATIONAL PROGRAM THAT ILLUSTRATES
#THE MULTIPLE INHERITANCE. THREE IS NOT NEEDED IN A REAL PROGRAM
#CLASSES TO MANAGE SIMPLE MATHEMATICAL OPERATIONS.
class a(object):
    def __init__(self,numero):
           self.numero = numero
    def seno(self):
        s=f'Sono nella classe a. Il seno di {self.numero} è {math.sin(self.numero)}'
        print(s)
    def coseno(self):
        s=f'Il coseno di {self.numero} è {math.cos(self.numero)}'
        print(s)
class b:
    def __init__(self,numero):
        self.numero = numero
    def tangente(self):
        s=f'La tangente di {self.numero} è {math.tan(self.numero)}'
        print(s)
    def arcotangente(self):
        s=f'L\'arco tangente di {self.numero} è {math.atan(self.numero)}'
        print(s)
    def seno(self):
        s=f'Sono nella classe b. Il seno di {self.numero} è {math.sin(self.numero)}'
        print(s)
    def radice(self):
        s=f'Sono nella classe b. La radice di {self.numero} è {math.sqrt(self.numero)}'
        print(s)
class calcolatrice(a,b):
    def __init__(self,numero,valore):
        super().__init__(numero)
        s=f'Sono nella classe derivata valore = {valore}'
        print(s)
c = calcolatrice(144,90)
c.seno()
c.radice()
s=f'MRO: {calcolatrice.__mro__}'
print(s)
#LA CLASSE TYPE E OBJECT
class MyClass(object):
    pass
myObj = MyClass()
print(isinstance(myObj,MyClass))
print(isinstance(myObj,object))
print(isinstance(myObj,type))
print(isinstance(MyClass,object))
print(isinstance(MyClass,type))
print(isinstance(object,object))
print(isinstance(object,type))
print(isinstance(type,type))
print(isinstance(type,object))