#na=open("G:\\Notepadd_python\\textdoc.txt","w+")
#na.write("G:\\Notepadd_python\\textdoc.txt")
#na=open("G:\\Notepadd_python\\textdoc.txt","r")
#print(na.read())


# with open("G:\\Notepadd_python\\textdoc.txt") as ld:
    # ldt=ld.read()
    # print(ldt)

# with open("nameoffile") as li:            #### 
    # liData=li.readlines()
    # print(liData)
    
f=open("G:\\Notepadd_python\\Routines in SAP BI 7.0 Transformation.0 Transformation.0 Transformation","w+")
fh=f.readlines() 
print(fh)
   
   
   
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)
   
    
import os 
print(os.listdir(".")) 



import pickle 
class Employee: 
    def __init__(self,eno,ename,esal,eaddr): 
        self.eno=eno; 
        self.ename=ename; 
        self.esal=esal; 
        self.eaddr=eaddr; 
    def display(self): 
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr) 
    with open("emp.dat","wb") as f: 
        e=Employee(100,"Durga",1000,"Hyd") 
        pickle.dump(e,f) 
        print("Pickling of Employee Object completed...") 
 
    with open("emp.dat","rb") as f: 
        obj=pickle.load(f) 
        print("Printing Employee Information after unpickling") 
        obj.display()     