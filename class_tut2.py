class Person:
    age = 26
    name = "shamyl"

    def set_name(self,input):
        self.name = input
        print("name_set: ", self.name)

    def greet(self):
        print("Hello ", self.name)

name_input = input("Enter your name: ")
Shamyl = Person()
Shamyl.set_name(name_input)

Shamyl.greet() 