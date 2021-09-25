def paridispari():
    inp = input("Inserisci un Numero")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("Numero Pari")
    else:
        print("Numero Dispari")
#Per eseguire il programma premere il tasto F1 e selezionare
#Python: Esegui file python nel terminale
paridispari()
