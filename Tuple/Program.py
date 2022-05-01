def Tuple():
    colori=()#LE PRIME DUE ISTRUZIONI SIGNIFICANO LA STESSA COSA
    colori=tuple()
    colori='rosso','verde','blu'
    colori=('rosso','verde','blu')
    #TUPLE UNPACKING (SPACCHETTAMENTO DI UNA TUPLA)
    a,b,c = colori
    print(a)
    print(b)
    print(c)
    t1=(1,2)
    t2=(3,4)
    mylist=[t1,t2]
    print(mylist)
    mylist.append((5,6))
    print(mylist)
Tuple()