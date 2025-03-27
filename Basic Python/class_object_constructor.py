class Info:
    # use this if need parameter in class
    def __init__(self, name):
        self.name = name

    def infofunc(self, age):
        print(self.name, age)

inf = Info('Hamja')
inf.infofunc(24)

class InforMation:
    def __init__(self):
        self.name = input("Enter Your name: ")
        self.age = input("Enter Your age: ")
    
    def showinfo(self):
        print(self.name, "Your age", self.age)
        # print("Your age is: ", self.age)

obj1 = InforMation()
obj2 = InforMation()
obj1.showinfo()
obj2.showinfo()

# show the memory address of the object
# print(id(inf))