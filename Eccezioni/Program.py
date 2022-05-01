def divisionbyzero(a,b):
    return a//b
try:
    c=divisionbyzero(9,3)
except (ZeroDivisionError,ValueError) as e:#You can indicate more classes of
    #exceptions on one line
    print("ERRORE DIVISIONE PER 0!")
    print(e.args)
except IndexError:
    print("INDEX ERROR!")
except Exception:
    print("ERRORE GENERICO!")
else:
    print(c)    
finally:
    print('FINALLY!')
#WE CAN DECIDE TO USE N CLASSES OF EXCEPTIONS
#IN THIS CASE, ERROR MANAGEMENT IS NOT MUCH
#ARTICULATED, THE PROGRAM IS LIMITED TO PRINTING A MESSAGE
#HOWEVER IN THIS CASE THE PROGRAM DOES NOT END IN WAY
#ANOMALO AND THERE IS NO RISING IN THE CALL STACK FOR
#FIND A VALID ERROR MANAGER. THE FINALLY CLAUSE
#IT IS ALWAYS PERFORMED NORMALLY IT IS USED FOR
#RELEASE RESOURCES FOR EXAMPLE CLOSE THE CONNECTION TO A DATABASE.

