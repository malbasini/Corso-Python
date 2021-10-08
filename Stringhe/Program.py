def stringhe():
    titolo="L'isola Misteriosa"
    autore="Giulio Verne"
    print(f"Titolo: {titolo.upper()}, Autore: {autore}.")
    #Gli operatori + e * possono essere utilizzati per la manipolazione di stringhe.
    #La precedenza tra gli operatori viene mantenuta.
    #CONCATENAZIONE
    a="Hello"
    print(a+a+a)
    print(a*4)
    #Le stringhe sono, come ogni entità in
    #Python , oggetti e dispongono di una
    #serie di funzionalità accessibili tramite dei metodi built in
    #split([sep, [maxsplit]])
    #replace(old , new[, count])
    #strip([chars])
    s="Ciao Mondo"
    print(s.split('a',1))
    print(s.replace('a','U',1))
    print(s.strip('C'))
    #Formattazione: allineamento, maiuscole, minuscole
    #center(width[, fillchar]) ,ljust[,fillchar ]), rjust[, fillchar ])
    #upper() ,lower()) ,swapcase()
    s="Questa è una STRINGA su una riga"
    print(s.center(50,'.'))
    print(s.ljust(50,'.'))
    print(s.lower())
    #RICERCA : ricerca e interrogazione sulla stringa
    #find(sub[,start[,end]])  index(sub[,start[,end]])
    #rindex(sub[,start[,end]])  rfind (sub[,start[,end]])
    #count(sub[, start[,end]])
    #isupper() islower()
    #startswith(prefix[,start[,end]]) ,endswith(prefix[,start[,end]])
    print(s.find('riga',0,50))
    print(s.index('u',0,5))
    print(s.count('a',0,50))
    print(s.rindex('a',0,50))
    #Una stringa vuota è valutata
    #False mentre qualsiasi stringa
    #non vuota è valutata True
    #Le funzioni
    #min , max e cmp possono essere utilizzate anche sulle
    #stringhe.
    #Le stringhe sono inoltre dotate dell’operatore
    #in e not in
    s='Hello'
    print(min(s),max(s))
    print('e' in s)


stringhe()