def While():
    #PRIMO ESEMPIO
    x=0
    while(x<3):#sino a che x<3 esegui la suite di while
        print(x)
        x+=1 #Incremento x per chiudere il Loop
             #e non ciclare all'infinito
             #stamperà 0,1,2
    else:
        print("Codice ramo else sempre eseguito.")
    #SECONDO ESEMPIO
    #Ci sono molti casi in cui non sappiamo a priori quante
    #volte deve essere eseguito un loop. Ad esempio:
    while True:#LOOP INFINITO
        x=input("Inserire una stringa: ")
        if x=='stop':
            break #LO STATEMENT BREAK INTERROMPE IMMEDIATAMENTE IL LOOP
        print(x)
    #TERZO ESEMPIO
    while True:#LOOP INFINITO
        x=input("Inserire una stringa: ")
        if x=='stop':
            break     #LO STATEMENT BREAK INTERROMPE IMMEDIATAMENTE IL LOOP
        if x <'b':
            continue  #CONTINUE NON INTERROMPE IL LOOP MA SI
                      #RITORNA IN TESTA AL LOOP STESSO
        print(x)
While() 
