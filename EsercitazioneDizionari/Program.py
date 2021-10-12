def esercitazione():
    d1={10: "a",20: "b"}
    print(type(d1))
    d2={30:"c"}
    print(type(d2))
    l1=d1.items()
    print(type(l1))
    print(l1)
    l2=d2.items()
    d3=dict(l1)#SI PUO' COSTRUIRE UN DIZIONARIO TRAMITE COSTRUTTORE
               #PARTENDO DAI SUOI ITEMS
    d3.update(dict(l2))
    print(d3)
esercitazione()
