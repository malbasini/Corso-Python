def Range():
    #Scrivere un algoritmo utilizzando un ciclo for
    #e la funzione range compresa tra 10 e 50 che 
    #aggiunge ad una lista
    #i numeri dispari compresi tra 10 e 40.
    lista=[]
    for x in range(10,50):
        if (x % 2 > 0) and (x < 40):
            lista.append(x)
    print(lista)        
Range()