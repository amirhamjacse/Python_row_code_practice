class Student:
    def __init__(self, name):
        self.name = name

    def showinfo(self):
        print(self.name)

class Students(Student):
    # if you want to use parent class's function then use
    def showinfo(self):
        return super().showinfo()
    # if you want to override then
    def showinfo(self):
        print(self.name, "method override")

obj1 = Student("Hamja")
obj1.showinfo()
obj2 = Students("Hamja")
obj2.showinfo()
