from typing import List
#Let's look at a couple of examples. The following three examples
# take two parameters and return their sum.
# As you can see, <expression> can be anything.
#All three are valid function definitions but it shows
#different ways to use function annotations.
#Note that if there are parameters with default values,
#notations must always precede the default value
#of a parameter as you saw in the third example below.
def func1(num1:str = "1st param", num2:str = "2nd param") -> str:
    return num1 + num2
def func2(num1: int, num2: int) -> int:
    return num1 + num2
def func3(num1: int, num2: int=10) -> int :
    return num1 + num2

print(func1('pippo','pluto'))
print(func2(20,30))
print(func3(80))
print(func2.__annotations__)

#Annotazioni di variabili
name: str
city: str = 'Mysor'
age: int = 35

# In the following example, the square function expects
# an integer parameter num and returns all squares
# the numbers from 0 to num. The squares variable is declared as
# List [int] to indicate that it contains a list of integers.
# Similarly, the return type of the function is also List [int].
# Next, square .__ annotations__ provides
# local annotations to the function and __annotations__ provides
# global annotations.


squares: List[int] = []
def square(num: int) -> List[int]:
    for i in range(num):
        squares.append(i**2)
    return squares
print(square(10))
print(square.__annotations__)
print(__annotations__)
#Class can also use data Annotations
class MyClass:
    nome: str
    cognome:str
    
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome

    def denominazione(self):
        print(f'{self.nome} {self.cognome}')

m=MyClass(nome='Mario',cognome='Rossi')
print(m.denominazione())
print(m.nome)
print(m.cognome)

