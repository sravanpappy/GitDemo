##########Oops Encapsulation


##### Private methods ##
# class car:
    # def __init__(self):
        # self.__updatesoftware()  ###private methods
    # def drive(self):
        # print("Driving")
    # def __updatesoftware(self):
        # print("update software")
       
# c=car()
# c.drive()       
     
#c.__updatesoftware() ------> ##Error 
##Error   ====> AttributeError: 'car' object has no attribute '__updatesoftware'
## do not call private method directly by using class



# class name:
    # def __init__(self):
        # self.__data()
   
    # def name(self):
        # print("This is onother mathod")
    # def __data(self):
        # print("This is privte method")
       
# a=name()
# a.name()


#####Privaye varibles ###
class car:
    __name=""
    __maxspeed=0
    def __init__(self):
        self.__name="BMW"
        self.__maxspeed=150
    def drive (self):
        print("Driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)
        
       
aa=car()
aa.drive()  
aa.setspeed(1505) 

import turtle
col=("red","yellow","green","cyan","pink","white")
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(25)
for i in range(150):
    
    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)



      