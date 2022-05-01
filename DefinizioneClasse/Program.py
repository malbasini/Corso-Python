class MyClass(object):
    counter=0 #servirà a contare quante istanze
              #vengono costruite sulla classe
              #counter in quanto definito nel body
              #della classe è un attributo di MyClass
    def __init__(self):
        MyClass.counter+=1 #Ogni volta che creiamo una
                           #nuova istanza, viene chiamato
                           #__init__ e incrementato il contatore
    
    @classmethod          
    def istanze(cls):
        print(cls.counter)
    #Definiamo un metodo che non è applicabile alle
    #singole istanze ma alla classe stessa
    #il decoratore @classmethod serve a questo scopo.
    #cls per convenzione indica l'oggetto classe 

m1 = MyClass()
m2 = MyClass()
m3 = MyClass()
MyClass.istanze() #stampa 3