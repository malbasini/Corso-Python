
class persona(object):
    def __init__(self,nome,cognome,indirizzo):
        self.__nome_ = nome
        self.__cognome_ = cognome
        self.__indirizzo_ = indirizzo
    @property
    def nome(self):
        return self.__nome_
    @nome.setter
    def nome(self,nome):
        self.__nome_ = nome
    @property
    def cognome(self):
        return self.__cognome_
    @cognome.setter
    def cognome(self,cognome):
        self.__cognome_ = cognome
    @property
    def indirizzo(self):
        return self.__indirizzo_
    @indirizzo.setter
    def indirizzo(self,indirizzo):
        self.__indirizzo_ = indirizzo
    def denominazione(self):
        s= f'Persona Nome: {self.nome} Cognome: {self.cognome} indirizzo: {self.indirizzo}'
        print(s)

class utente(persona):
        def __init__(self,id,numeroconto,saldo,nome,cognome,indirizzo):
            self.__id_ = id
            self.__numeroconto_ = numeroconto
            self.__saldo_ = saldo
            super().__init__(nome,cognome,indirizzo)
        @property
        def id(self):
            return self.__id_
        @id.setter
        def id(self,id):
            self.__id_ = id
        @property
        def numeroconto(self):
            return self.__numeroconto_
        @numeroconto.setter
        def numeroconto(self,numeroconto):
            self.__numeroconto_ = numeroconto
        @property
        def saldo(self):
            return self.__saldo_
        @saldo.setter
        def saldo(self,saldo):
            if (saldo < 0):
                s=f'Impossibile impostare il saldo, valore passato: {saldo}'
                print(s)
                return
            else:
                self.__saldo_ = saldo
        def saldoCorrente(self):
            s = f'Utente: nome {self.nome} cognome {self.cognome} saldo {self.saldo}'
            print(s)

class banca():
        def __init__(self,id,denominazione,abi,cab,utente):
            self.__id_=id
            self.__denominazione_=denominazione
            self.__abi_=abi
            self.__cab_ = cab
            self.__utente_=utente
        @property
        def id(self):
            return self.__id_
        @id.setter
        def id(self,id):
            self.__id_ = id
        @property
        def denominazione(self):
            return self.__denominazione_
        @denominazione.setter
        def denominazione(self,denominazione):
            self.__denominazione_ = denominazione
        @property
        def abi(self):
            return self.__abi_
        @abi.setter
        def abi(self,abi):
            self.__abi_ = abi
        @property
        def cab(self):
            return self.__cab_
        @cab.setter
        def cab(self,cab):
            self.__cab_ = cab
        @property
        def utente(self):
            return self.__utente_
        @utente.setter
        def utente(self,utente):
            self.__utente_ = utente
        def preleva(self,importo,utente):
            if importo < 0 or importo > utente.saldo:
               s = f'Impossibile prelevare, importo passato: {importo} saldo: {utente.saldo}'
               print(s)
               return 
            else:
               utente.saldo -= importo
        def accredita(self,importo,utente):
            if importo < 0:
                s = f'Impossibile accreditare, valore passato: {importo}'
                print(s)
                return 
            else:
                utente.saldo += importo

u1 = utente(12345,"AS67890OL",12000.0,'Mario','Rossi','via delle rose 54')
u2 = utente(678345,"AS67L768",2000.0,'Luigi','Verdi','via della fontana 7')
u1.denominazione()
u2.denominazione()
u1.saldoCorrente()
u2.saldoCorrente()
b1=banca(9873456,'UBI BANCA', 30600,10400,u1)
b2=banca(9876832,'UBI BANCA', 30600,10400,u2)
b1.preleva(5000.0,u1)
u1.saldoCorrente()
b2.accredita(3000.0,u2)
u2.saldoCorrente()

