from dataclasses import dataclass
#A partire dalle annotazioni di tipo Python è in grado di inferire
#la presenza di tipi di oggetto Field che rappresentano i campi della classe
@dataclass(init=True,repr=True,order=True,frozen=False)
class MyClass(object):
    nome: str
    cognome: str

mc1=MyClass(nome='Luigi',cognome='Rossi')
#Il metodo repr facendo una print(mc) ci fornisce una stampa più compatta.
print(mc1)
mc2=MyClass(nome='Luigi',cognome='Rossi')
print(mc2)
print(mc1<mc2)
print(mc1>mc2)
print(mc1==mc2)

