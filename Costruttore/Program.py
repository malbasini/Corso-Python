class animale():
    def __new__(cls):
        istanza1 = super().__new__(cls)
        print(f'Istanza animale creata')
        return istanza1
    def __init__(self):
        print(f'Istanza animale inizializzata')
    def mangia(self):
        pass
    def respira(self):
        pass
class mammifero(animale):
    def __new__(cls,nome):
        istanza2 = super().__new__(cls)
        print(f'Istanza {nome} creata')
        return istanza2
    def __init__(self,nome):
         super().__init__()
         self.nome=nome
         print(f'Istanza {nome} inizializzata')
    def mangia(self):
        print(f'Classe mammifero istanza {self.nome} sta mangiando')
    def respira(self):
        print(f'Classe mammifero istanza {self.nome} sta respirando')
class persona(mammifero):
    def __new__(cls,nome,nomepersona,cognome):
        print(nomepersona)
        print(cognome)
        istanza3 = super().__new__(cls,nome)
        return istanza3
    def __init__(self,nome,nomepersona,cognome):
        super().__init__(nome)
        self.nomepersona=nomepersona
        self.cognome=cognome

    def denominazione(self):
        print(f'Classe persona denominazione : {self.nomepersona} {self.cognome}')
        
p = persona('persona','Luigi','Rossi')
p.denominazione()
p.mangia()
p.respira()
