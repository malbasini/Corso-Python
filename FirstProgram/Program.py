def paridispari():
    inp = input("Inserisci un Numero ")
    numero = int(inp)
    modulo = numero % 2
    if modulo == 0:
        print("Numero Pari")
    else:
        print("Numero Dispari")
#To run the program type in the terminal
#python or python3 (look at the Python installation directory
#to know which command to use)
#followed by a space and the program name .py.
#In this case python Program.py
paridispari()        

