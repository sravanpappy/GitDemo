# class car:

    # whells = 4

    # def __init__(self):
        # print("default const")
    
    # def __init__(self, color):
        # print("car class constrctor")
        # self.color=color
    
    # def test(self):
        # print("test method")
    
    # def setprice(self, price):
        # self.price=price
    
    # def getprice(self):
        # return self.price

# c1=car('white')
# print(c1.whells)
# print(car.whells)

# c1.test()
# c1.setprice(50)
# print(c1.getprice())
# c2=car("brand")

# class names:
    # no_of_students = 50
    #def __int__ (self):
       # print ("total stundents of int")
    # def __init__(self, names):
        # print("name of the student")
    # def sno(self):
        # print("student no")
    # def snames(self, addmarks):
        # self.addmarks=addmarks
    # def totalmarks(self):
        # return self.addmarks

# name=names("sravan")        
# print(name



class Person:  
    #initializing the variables  
    name = ""  
    age = 0  
      
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
          
    #end of the class definition  
  
# Create an object of the class  
person1 = Person("John", 23)  
#Create another object of the same class  
person2 = Person("Anne", 102)  
#call member methods of the objects  
person1.showAge()  
person2.showName()