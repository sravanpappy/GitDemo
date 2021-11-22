

class employee:
    def __init__(self,eno,ename,esalary):
        self.eno=eno
        self.ename=ename
        self.esalary=esalary
    def display(self):
        print("employee number:",self.eno)
        print("employee name:",self.ename)
        print("employee salary:",self.esalary)
       
class Test:
        def modify(emp):
            emp.esalary=emp.esalary+10000
            emp.eno = 101
            emp.display()
           
e=employee(100,"sravan",100)  
Test.modify(e)         