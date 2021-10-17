def Statement():
    #PRIMO ESEMPIO
    x=8
    if x<10: #Si legge "se x minore di 10 
             #allora stampa a video Minore di 10"
        print("Minore di 10")
    #SECONDO ESEMPIO
    x=10
    if x<10:#Si legge:Se x<10 (test booleano) allora stampa Minore di 10
            #else (altrimenti stampa >=10)
        print("Minore di 10")
    else:
        print("Maggiore o uguale a 10")
    #TERZO ESEMPIO
    x=6
    if x<5:               #se x<5
        print("< di 5")
    elif (x>=5 and x<=10):# altrimenti se x compreso tra 5 e 10
        print(">=5 e <= a 10")
    else:                 #altrimenti in tutti gli altri casi > di 10
        print("> di 10")
Statement()
