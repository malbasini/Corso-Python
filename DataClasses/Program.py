from dataclasses import dataclass
#Starting from annotations of type Python is able to infer
#the presence of Field object types that represent the fields of the class
@dataclass(init=True,repr=True,order=True,frozen=False)
class MyClass(object):
    nome: str
    cognome: str

mc1=MyClass(nome='Luigi',cognome='Rossi')
# The repr method doing a print(mc) gives us a more compact print.
print(mc1)
mc2=MyClass(nome='Luigi',cognome='Rossi')
print(mc2)
print(mc1<mc2)
print(mc1>mc2)
print(mc1==mc2)

