# class student:
	# no_of_st = 10
	
	# def name(self):
		# print("sravan")
        
# d=student()
# d.name()


class person:
    name = ""
    age = 0
    def __init__(self, personname, personage):
        self.name=personname
        self.age=personage
    def showname(self):
        print(self.name)
    def showage(self):
        print(self.age)
        
person1=person('sravan',23)
person2=person('natha',100)

print(person1.showage())
print(person1.showname())



class Person:         
    name = "John"      
    age = 24  
    def display (self):      
        print("Age: %d \nName: %s"%(self.age,self.name))      
# Creating a emp instance of Employee class    
per = Person()      
per.display()


xx=50
def var_test():
    xx=100
    return xx
print(var_test())






