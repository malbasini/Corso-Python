def Set():
    myset = set()#CREIAMO UN INSIEME VUOTO
    myset = set([10,20,30,40])#CREIAMO UN INSIEME INIZIALIZZATO
    myset={10,20,30,40}#CREIAMO UN INSIEME INIZIALIZZATO
    #myset{} ERRORE STIAMO CREANDO UN DIZIONARIO VUOTO
    myset=set()
    myset.add(10)
    myset.add(20)
    myset.add(30)
    myset.add(40)
    myset=frozenset([10,20,30])
    #myset.add(40) ERRORE
    print(30 in myset)
    #print(myset)
    myset=set([10,20,30,40])
    myset2=set([30,40,50])
    print(myset & myset2)#OPERAZIONE DI INTERSEZIONE
    print(myset | myset2)#OPERAZIONE DI UNIONE
    print(myset - myset2)#OPERAZIONE DIFFERENZA
    print(myset ^ myset2)#XOR

Set()    
