
# class Student:
        # """This is preparing for the instance varible"""
        # def __init__(self,name,age):
            # self.name=name
            # self.age=age
        # def fin (self):
            # #self.marks=60
            # del self.name
           
# s1=Student("Sravan",25)
# s1.fullname="Ganga"
# s1.name="ganagdevunipalle sravan kuamr"
# del s1.age
# print(s1)
# print(s1.fin())
# print(s1.__dict__)  


class delte:
    """This is used for the deletion"""
    def __init__(self):
        self.a=100
        self.b=200
        self.c=300
    def d(self):
        namee=155
        del self.a, self.b
       
a=delte()
print(a.__dict__)
a.d()
print(a.__dict__)     
       
