class persona():
    def __init__(self,nome,cognome,eta):
        self.__nome__= nome
        self.__cognome__= cognome
        self.__eta__ = eta
    @property
    def nome(self):
        return self.__nome__
    @nome.setter
    def nome(self,nome):
        self.__nome__ = nome
    @property
    def cognome(self):
        return self.__cognome__
    @cognome.setter
    def cognome(self,cognome):
        self.__cognome__ = cognome
    @property
    def eta(self):
        return self.__eta__
    @eta.setter
    def eta(self,eta):
        self.__eta__ = eta
    def denominazione(self):
        s= f'Persona Nome: {self.nome} Cognome: {self.cognome} età: {self.eta}'
        return s

class studente(persona):
    def __init__(self,nome,cognome,eta,facolta,anno):
        self.__facolta__= facolta
        self.__anno__= anno
        super().__init__(nome,cognome,eta)
    @property
    def facolta(self):
        return self.__facolta__
    @facolta.setter
    def facolta(self,facolta):
        self.__facolta__ = facolta
    @property
    def anno(self):
        return self.__anno__
    @anno.setter
    def anno(self,anno):
        self.__anno__ = anno
