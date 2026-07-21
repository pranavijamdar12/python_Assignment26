class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter the first number: "))
        self.value2 = int(input("Enter the second number: "))

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        if self.value2 == 0:
            return "Division by zero is not possible."
        return self.value1 / self.value2

    def Display(self):
        print("Addition is :", self.Addition())
        print("Subtraction is :", self.Subtraction())
        print("Multiplication is :", self.Multiplication())
        print("Division is :", self.Division())


# First Object
Obj1 = Arithmetic()
Obj1.Accept()
Obj1.Display()

print("--------------------------------")

# Second Object
Obj2 = Arithmetic()
Obj2.Accept()
Obj2.Display()
