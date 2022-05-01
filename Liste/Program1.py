def Lista():
    mylist=[] #Crea una lista vuota
    mylist=[1,2,3,4,5,6] #Inizializza una lista con degli interi
    mylist= list() #Chiama il costruttore della classe list per
                   #creare una lista vuota. Equivale alla prima dichiarazione.
    mylist=[1,2,3,4,5,6] #Si parte dall'offset 0 (indice)
    print(mylist[0])
    print(mylist[-1]) #Se vogliamo partire dal fondo della lista usiamo
                      #indici negativi.
    mylist = [[1,2],[3,4],[4,5]] #Liste di liste
    print(mylist[1][0])
    mylist=[1,2,3,4,5,6]
    mylist[0] = 10 #Le liste sono oggetti mutabili. Quindi possiamo
                   #Modificarne i valori
    print(mylist[0])
    #SLICE DI UNA LISTA E' POSSIBILE ESTRARRE PARTI DI UNA LISTA
    #GLI SLICE LI ABBIAMO VISTI NELLE STRINGHE. QUI' VALGONO LE
    #STESSE CONSIDERAZIONI
    print(mylist[:2])
    #ESISTE UNA FUNZIONE PREDEFINITA IN PYTHON len CHE RESTITUISCE
    #LA LUNGHEZZA DELLA LISTA
    print(len(mylist))
    #INSERIMENTO DI ELEMENTI NELLA LISTA STIAMO CHIAMANDO UN METODO
    #DELLA CLASSE LIST CON LA DOT NOTATIONS PER INSERIRE IL NUMERO 50
    #ALL'OFFSET 2
    mylist.insert(2,50)
    mylist.append(100)#METODO APPEND AGGIUNGE IN CODA ALLA LISTA
    del mylist[2] #CONSENTE DI ELIMINARE UN ELEMENTO DA UNA LISTA
    print(100 in mylist)
    mylist=[1,2,3,4,5,6]
    #mylist2=mylist
    #mylist2[0]=10
    mylist2=mylist.copy()
    mylist2[0]=10
    print(mylist)
    print(mylist2)
Lista()