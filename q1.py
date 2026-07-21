class Demo:
    Value = 100 #class variable
    def __init__(self,no1,no2):
        self.no1 = no1 # instance variable
        self.no2 = no2

    def Fun(self):
        print("Fun Method:")
        print("No1 =",self.no1)
        print("No2 =",self.no2)

    def Gun(self):
        print("Gun Method:")
        print("No1 =",self.no1)
        print("No2 =",self.no2)

obj1=Demo(11,21) # object is created
obj2=Demo(51,100)

obj1.Fun()
obj2.Fun() # function call
obj1.Gun()
obj2.Gun()

    
