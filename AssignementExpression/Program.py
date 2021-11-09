
class MyClass(object):
    def __new__(cls,list):
        istanza = super().__new__(cls)
        print(f'Istanza creata')
        return istanza
    def __init__(self,list):
        self.list = list
    def example1(self):
        #Using assignment expressions in if statements
        if (length := len(self.list)) > 2:
            print("List length of", length, "is too long")
    @staticmethod
    def example2():
        #Use assignment expressions in loops
        while (directive := input("Enter text: ")) != "stop":
            print("Received directive", directive)
    @staticmethod
    def example3(x):
        print("Multiplying", x, "*", x)
        return x * x

l=[1,2,3,4,5]
e=MyClass(l)
e.example1()
MyClass.example2()
#Using assignment expressions in ranges
[result for i in range(6) if (result := MyClass.example3(i)) > 0]
