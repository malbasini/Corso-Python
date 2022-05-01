class String(object):
    def __new__(cls,nome):
        istanza = super().__new__(cls)
        print(f'Istanza creata')
        return istanza
    def __init__(self,nome):
        self.nome=nome
    def rStrip(self,sottostringa):
        #DELETE CHARACTERS ON THE RIGHT. A STRING IS RETURNED
        #IN CASE OF SUCCESS SHORTER THAN THE ORIGINAL ONE
        print(f'rstrip: {self.nome.rstrip(sottostringa)}') 
    def strip(self,spazi,sottostringa):
        if spazi == False:
            print(f'strip: {self.nome.strip(sottostringa)}')
        else:
             #LEAVING THE PARENTHESES EMPTY, SPACES ARE ELIMINATED
             #RIGHT AND LEFT
            print(f'strip: {self.nome.strip()}')
    def lStrip(self,sottostringa):
        print(f'lstrip: {self.nome.lstrip(sottostringa)}')
    def removePrefix(self,sottostringa):
        print(f'removeprefix: {self.nome.removeprefix(sottostringa)}')
    def removeSuffix(self,sottostringa):
        print(f'removesuffix: {self.nome.removesuffix(sottostringa)}')

a = String("remore e tenore")
a.rStrip('re')
a.strip(False,'re')
a.lStrip('re')
b=String("   Mario Rossi  ")
b.strip(True,'')
#A SIDE EFFECT OF THESE METHODS THAT SOMETIMES HAS
#GENERATED MISUNDERSTANDING AMONG THE PROGRAMMERS IS DUE TO FACT
#THE PASSING THE REVERSE SEQUENCE 'er' INSTEAD OF '' re 'WE GET IT
#SAME RESULT. THIS IS DUE TO THE FACT THAT THESE THREE FUNCTIONS
#THEY USE A SET OF CHARACTERS NOT STRINGS. THE PRESENCE
#OF THESE CHARACTERS APPLIED IN ANY SEQUENCE IT CAUSES
#SAME BEHAVIOR.
#a.rStrip('er')
#a.strip(False,'er')
#a.lStrip('er')
a.removePrefix('re')
a.removePrefix('er')
a.removeSuffix('re')
a.removeSuffix('er')
