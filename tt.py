class car:

    whells = 4

    # def __init__(self):
        # print("default const")
    
    # def __init__(self, color):
        # print("car class constrctor")
        # self.color=color
    
    def test(self):
        print("test method")
    
    def setprice(self, price):
        self.price=price
    
    def getprice(self):
        return self.price
	
# c1=car('white')
# print(c1.whells)
# print(car.whells)

# c1.test()
# c1.setprice(50)
# print(c1.getprice())
# c2=car("brand")
c2=car()
print(c2.test())





