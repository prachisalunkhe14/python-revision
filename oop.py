class person:
    __name = "Prachi"

    def __hello(self):
        print("hello person")

    print(__name)

    def wel_come(self):
        self.__hello()
    
p1 = person()

p1.wel_come()