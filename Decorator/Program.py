def myDecorator(f):
    def decorator():
        print('Ho decorato')
        f()
    return decorator

@myDecorator
def myFunc():
    print('La Funzione myFunc')

myFunc()