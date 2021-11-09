class String(object):
    def __new__(cls,nome):
        istanza = super().__new__(cls)
        print(f'Istanza creata')
        return istanza
    def __init__(self,nome):
        self.nome=nome
    def rStrip(self,sottostringa):
        #ELIMINA CARATTERI A DESTRA. VIENE RESTITUITA UNA STRINGA
        #IN CASO DI SUCCESSO PIU' CORTA DI QUELLA DI ORIGINE
        print(f'rstrip: {self.nome.rstrip(sottostringa)}') 
    def strip(self,spazi,sottostringa):
        if spazi == False:
            print(f'strip: {self.nome.strip(sottostringa)}')
        else:
            #LASCIANDO VUOTE LE PARENTESI VENGONO ELIMINATI SPAZI
            #A DESTRA E SINISTRA
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
#UN EFFETTO COLLATERALE DI QUESTI METODI CHE TALVOLTA HA
#GENERATO INCOMPRENSIONE TRA I PROGRAMMATORI E' DOVUTA AL FATTO
#CHE PASSANDO LA SEQUENZA INVERSA 'er' ANZICHE' 're' OTTENIAMO LO
#STESSO RISULTATO. QUESTO E' DOVUTO AL FATTO CHE QUESTE TRE FUNZIONI
#USANO UN INSIEME DI CARATTERI NON DELLE STRINGHE. LA PRESENZA
#DI QUESTI CARATTERI APPLICATI IN UNA QUALSIASI SEQUENZA PROVOCA
#LO STESSO COMPORTAMENTO.
#a.rStrip('er')
#a.strip(False,'er')
#a.lStrip('er')
a.removePrefix('re')
a.removePrefix('er')
a.removeSuffix('re')
a.removeSuffix('er')
