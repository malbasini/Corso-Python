def For():
    #PRIMO ESEMPIO
    myList = [3,4,5,6,7,8]
    for x in myList:
        print(x)
    else:
        print("Ramo else sempre esguito.")
    #SECONDO ESEMPIO
    myString = "Hello"
    for x in myString:
        print(x)
    #TERZO ESEMPIO
    myDict = {"a":1,"b":2,"c":3}
    for x in myDict:
        print(x)#STAMPA LE CHIAVI
    for x in myDict.values():
        print(x)#STAMPA I VALORI
    for x in myDict.items():
        print(x)#STAMPA CHIAVI E VALORI
    #LE PAROLE CHIAVE BREAK E CONTINUE FUNZIONANO ALLO STESSO
    #MODO VISTO NEL CICLO WHILE
For()

