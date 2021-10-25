class MyClass():
    def __init__(self,nome):
        self.__nome_ = nome
    @property
    def nome(self):
        return self.__nome_
    @nome.setter
    def nome(self,nome):
        self.__nome_ = nome

m1 = MyClass('Marco')
print(m1.nome)
m1.nome="Luigi"
print(m1.nome)