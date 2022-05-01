

class Dictionary(object):
    def __new__(cls,d1,d2):
        istanza = super().__new__(cls)
        print(f'Istanza creata')
        return istanza
    def __init__(self,d1,d2):
        self.d1 = {"a":"primo","b":"secondo","c":"terzo"}
        self.d2 = {"d":"quarto","a":"quinto"}
    def stampa(self):
        print(self.d1)
        print(self.d2)
    def merge(self):
        self.d3 = self.d1.copy()
        for chiave, valore in self.d2.items():
            self.d3[chiave]=valore
        print(self.d3)
    def operatoreUnion(self):
        self.d3 = self.d1 | self.d2
        print(f'Operatore Union applicato a d1 e d2 d3= {self.d3}')
    def inPlaceOperatore(self):
        #Unisce il secondo dizionario d2 al primo d1
        self.d1 |= self.d2
        print(f'Operatore Self In Place Union applicato a d1 e d2 d1= {self.d1}')

a=Dictionary([],[])
a.stampa()
a.merge()
#Suppose to insert the key a already present in d1
#the result as you can see is that this will overwrite
#the "a" key of d1.
a.operatoreUnion()
a.inPlaceOperatore()
    