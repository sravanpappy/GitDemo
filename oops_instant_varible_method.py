# ###### Static methos 

# class employee:
    # def __init__(self,eno,ename,esalary):
        # self.eno=eno
        # self.ename=ename
        # self.esalary=esalary
    # def display(self):
        # print("emp number:",self.eno)
        # print("employee name:",self.ename)
        # print("employee salary:",self.esalary)
       
# class Test:
        # def modify(emp):
            # emp.esalary=emp.esalary+10000
            # emp.display()
            
# name=input("enter student name")
# no=int(input("Enter Student number:"))
# salary=float(input("Enter salary:"))

           
# e=employee(no,name,salary)
# Test.modify(e)           
        
        
   
# print("*"*25)   
# class outer:
        # def __init__(self):
            # print("Outer class object creation----")
            
        # class inner:
            # def __init__(self):
                # print("Inner class object creatin___")
            # def m1(self):
                # print("Inner class method")
               
# # a=outer()
# # b=a.inner()
# # c=b.m1()

# outer().inner().m1()


class employee:
    def __init__(self,eno,ename,esalary):
        self.eno=eno
        self.ename=ename
        self.esalary=esalary
        
    def disply(self):
        print("employee no:",self.eno)
        print("employee name:",self.ename)
        print("Employee salry:",self.esalary)
       
class Test:
        def modify(emp):
            emp.esalary=emp.esalary+555
            emp.display()
           
e=employee(100,"Sravan",10000)
Test.modify(e)           



               