def Dizionari():
   mydict = {}
   mydict = dict()#LE DUE DICHIARAZIONI SONO EQUIVALENTI
   mydict={"primo":20,"secondo":30,"terzo":40} #CREAZIONE E INIZIALIZZAZIONE
   mydict["quarto"]=50 #LA CHIAVE NON ESISTE. VIENE AGGIUNTO
                       #L'ELEMENTO AL DIZIONARIO
   mydict["quarto"]=60 #MODIFICA DI UN VALORE
   del mydict["secondo"] #ELIMINAZIONE DI UN VALORE
   print(mydict)
   print("terzo" in mydict)#RITORNA TRUE
   mydict.clear()#RIMUOVE TUTTE LE CHIAVI E TUTTI I VALORI
   mydict={}     #RIMUOVE TUTTE LE CHIAVI E TUTTI I VALORI
Dizionari()