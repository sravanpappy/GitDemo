####instant methos

# class student:
    # def __init__(self,name,marks):
        # self.name=name
        # self.marks=marks
       
    # def display (self):
        # print("Hi",self.name)
        # print("Your marks are:",self.marks)
       
    # def grade(self):
        # if self.marks>=60 and self.marks<=100:
            # print("First Grade")
        # elif self.marks >=50 and self.marks<=59:
            # print("Second Class")
        # elif self.marks >=35 and self.marks <=49:
            # print("Third Class")
        # elif self.marks>=0 and self.marks <=34:
            # print("Fail")
        # else:
            # print("Sorry you i am not recarnize")
           
# n=int(input("Enter No of Students:"))
# for i in range(n):
    # name=input("Enter student Name:")
    # marks=int(input("Enter Student marks:"))
    # s=student(name,marks)
    # s.display()
    # s.grade()    
    # print("*"*20)
   
	
class percentage:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
       
    def display(self):
        print("hi",self.name)
        print("Your percentage",self.marks)
    def perc(self):
        if self.marks >=60:
            print("Your first class:")
        elif self.marks >=50:
            print("Your second class")
        elif self.marks >=35:
            print("You are just pass")
        else:
            print("Yor are fail")
          
n=int(input("Enter no of students:="))
for i in range(n):
            name=input("Enter Student Name:-")
            marks=int(input("Enter student marks:-"))
            s=percentage(name,marks)
            s.display()
            s.perc()
            print("*@"*5)
         
         