def paridispari():
    inp = input("Inserisci un Numero")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("Numero Pari")
    else:
        print("Numero Dispari")

paridispari()        

