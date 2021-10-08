def numeri():
    a = 123456789
    print(a)
    a=-800
    print(a)
    a=1_000_000  #L'underscore verrà ignorato. Introdotto
                 #in Python 3 con lo scopo di migliorare la lettura.
    print(bin(100))
    print(a)
    a=0b11001111        #numero binario
    print(a)
    a=0o1635            #numero ottale
    print(a)
    a=0x1ff             #numero esadecimale
    print(a)
    #Type = float
    a=0.0
    print(a)
    a=100.67
    print(a)
    a=-100.67
    print(a)
    a=10e+3
    print(a)
    a=10e-6
    print(a)

numeri()