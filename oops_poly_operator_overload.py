######operator over loading part 2#####


# class Book:
    # def __init__(self,pages):
        # self.pages=pages
        
    # def __str__(self):
        # return "Total no of pages:"+ str(self.pages)
     
    # def __add__(self,other):
        # total=self.pages+other.pages
        # b=Book(total)
        # return b
      
    # def __mul__(self,other):
        # total=self.pages*other.pages
        # b=Book(total)
        # return b 
    # def __sub__(self,other):
        # total=self.pages-other.pages
        # b=Book(total)
        # return b        
       
# b1=Book(5000)
# b2=Book(2050)
# a=Book(0)

# print(b1*b2+a)


### Employee Salary #######
# class Employee:
    # def __init__(self,name,salary):
        # self.name=name
        # self.salary=salary
        
    # def __mul__(self,other):
        # return self.salary*other.days
        
       
# class Timesheet:
        # def __init__(self,name,days):
            # self.name=name
            # self.days=days
           
# e=Employee("Sravan",750)
# t=Timesheet("Sravan",26)
# print("Total month salary:",e*t)           
        
            
# def fun():
    # pass
   
# print(type(fun())) 


class property:
    def p(self):
        print("land+gold+money")
    def marry(self):
        print("aaaah")
        
    
class son(property):
    pass
        # def marry(self):
            # print("chhhhhhha")
           
c=son()
c.p()
c.marry()           
        
        
       
      
