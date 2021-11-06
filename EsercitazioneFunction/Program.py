#DEFINE A FUNCTION THAT SELECTS THE DISTINCT ELEMENTS
#OF TWO LISTS. THE SECOND HAS DEFAULT VALUE [6,7,8,9,10].
#COLCULAR SUM AND SQUARE ROOT OF THE SELECTED ELEMENTS.
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
