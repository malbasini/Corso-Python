#CREARE LA SEGUENTE STRUTTURA DI DIRECTORY dir_a/dir_b/dir_c
#INSERIRE Modulo1 e Modulo2 in dir_c. CREARE LA VARIABILE D'AMBIENTE
#PYTHONPATH CHE PUNTA A dir_a.


#FILE myScript.py
import dir_b.dir_c.Modulo1 as m1
import dir_b.dir_c.Modulo2 as m2
#MODULO1
result = m1.numeroPrimo(11)
print(result)
#MODULO2
s = m2.studente('Mario','Rossi',23,'Giurisprudenza',2021)
v = s.denominazione()
print(v)