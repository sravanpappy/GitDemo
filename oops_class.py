

#######OOps Concept

# class emp:
        # "Employee data"
        # def __init__(self,empno,empname):
            # self.empno=empno
            # self.empname=empname
           
        # def name (self):
            # print(self.empno)
            # print(self.empname)
           
# a=emp(10,"sr")
# a.name()
# print(emp.__doc__) 


class student:
    """This is stored student data please find below details"""
    sid=0
    name=" "
    sph= 0
    def __init__(self,sid,name,sph):
        self.sid=sid
        self.name=name
        self.sph=sph
        
    def data(self):
        print("Student id:_",sid)
        print("student name:-",name)
        print("student ph number:-",sph)
     
    def getcollege (cls):
        print(cls.college)
       

print(student.__doc__)       
   
a=student(100,"Sravan",96400)
print(a.sph)
print(a.name)
print(a.sid)
a.data()