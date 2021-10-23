import math
#ELEVAMENTO A POTENZA
f=lambda x,y:math.pow(x,y)
print(f(2,3))
#SENO DI UN NUMERO
f=lambda v:math.sin(v)
print(f(180))
#STAMPA LA RADICE QUADRATA DI UN NUMERO PASSATO COME ARGOMENTO
f=lambda x:math.sqrt(x)
print(f(144))
#CONCATENA DUE VALORI
f=lambda s1,s2:s1+s2
print(f('Hello ','World!'))
#FUNZIONI RICORSIVE CALCOLO DEL FATTORIALE
#DI UN NUMERO
def fattoriale(n):
    """Il fattoriale di un numero
    indica il prodotto di
    quel numero per tutti i suoi antecedenti"""
    if n == 1:
        return 1
    else:
        return (n * fattoriale(n-1))
res = int(input("Inserisci un numero: "))
if res >= 1:
   print("Il fattoriale di", res, "è", fattoriale(res))