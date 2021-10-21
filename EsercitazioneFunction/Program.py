#DEFINIRE UNA FUNZIONE CHE SELEZIONA I DISTINTI ELEMENTI
#DI DUE LISTE. LA SECONDA HA DEI PARAMETRI DI DEFAULT [6,7,8,9,10].
#COLCOLARE SOMMA E RADICE QUADRATA DEGLI ELEMENTI SELEZIONATI.
import math
def funcliste(l1,l2=[6,7,8,9,10]):
    lresult=[]
    somma=0
    for x in l2:
        if not x in l1:
            lresult.append(x)
            somma+=x
    for x in l1:
        if not x in l2:
            lresult.append(x)
            somma+=x
    print(f'Risultato: {lresult}')
    print(f'Somma: {somma}')
    print(f'Radice Quadrata: {math.sqrt(somma)}')
    return lresult
funcliste([1,2,3,4,5],[2,4,8])
