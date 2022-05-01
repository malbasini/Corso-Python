class BClass:
    def __init__(self,message):
       self.message = message
    
    def printMessage(self):
        print(self.message)

    myString='Ereditarietà in Pyhon'

class AClass(BClass):
    def __init__(self,message,valore):
        super().__init__(message)#INIZIALIZZIAMO MESSAGE 
        #TRAMITE UNA CHIAMATA AL COSTRUTTORE DELLA SUPERCLASSE
        self.valore=valore

    def printMessage(self):
        super().printMessage()#Chiamata a printMessage di BClass

m1 = AClass('Python programming',100)
print(m1.valore)#stampa 100
print(m1.myString)#Attributo ereditato stampa 'Ereditarietà in Pyhon'
m1.printMessage()#stampa 'Python programming'
