from typing import List
#Diamo un'occhiata a un paio di esempi. I tre esempi seguenti 
#accettano due parametri e restituiscono la loro somma. 
#Come puoi vedere, <expression> può essere qualsiasi cosa. 
#Tutte e tre sono definizioni di funzioni valide ma mostra 
#diversi modi di utilizzare le annotazioni di funzione.
#Nota che se ci sono parametri con valori predefiniti, 
#le annotazioni devono sempre precedere il valore predefinito 
#di un parametro come hai visto nel terzo esempio sotto riportato.
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

# Nell'esempio seguente, la funzione quadrato si aspetta 
# un parametro intero num e restituisce i quadrati di tutti 
# i numeri da 0 a num. La variabile squares è dichiarata come 
# List [int] a indicare che contiene un elenco di numeri interi. 
# Allo stesso modo, anche il tipo restituito dalla funzione è List [int] . 
# Successivamente, square .__ annotations__ fornisce 
# annotazioni locali alla funzione e __annotations__ fornisce 
# annotazioni globali. 


squares: List[int] = []
def square(num: int) -> List[int]:
    for i in range(num):
        squares.append(i**2)
    return squares
print(square(10))
print(square.__annotations__)
print(__annotations__)
#Anche le classi possono usare le data Annotations
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

