#*******************************************************************
#IL METODO VERIFICA SE IL NUMERO PASSATO IN INPUT
#E' UN NUMERO PRIMO


#Modulo1.py
def numeroPrimo(numero):
    divisore = 2
    while divisore <= numero:
        risultato = numero//divisore
        if divisore > risultato:
            s=f'{numero} non è un numero primo.'
            return s
        if numero % divisore > 0:
            divisore+=1
            continue
        else:
            s=f'{numero} è un numero primo.'
            a=f'divisore: {divisore}'
            c=f'resto: {numero % divisore}'
            print(a)
            print(c)
            return s



