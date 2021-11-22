

####
import re

no = (r'(\d{1,3}\W\d{1,3}\W\d{2}\W\d{2})')
f2 = open("G:\\Notepadd_python\\reg_pro.txt","r+")

#print(f2.readline())

for line in f2:
    out = re.findall(no,line)
                                                           #####VVVVIMP
    for i in out : 
        print(i)
              
        

print("________________________________")



# new=re.findall(r'(\d{1,3}\W\d{1,3}\W\d{2}\W\d{2})',f2)
# print(new)

s="sivaramanatha 123hello"
 
r = re.findall('\d..',s)
print(r)




print("___________________")


   
  
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'  
# email=input("Enter email addres:-")  
# def check(email):   
  
    # if(re.search(regex,email)):   
        # print("Valid Email","____",email)   
    # else:   
        # print("Invalid Email",email)         
   
# check(email) 

print("____________")

m=input("enter email id:--")
regex = r"^[a-zA-Z]+[a-zA-Z0-9\.\-]+[@]+[a-zA-Z]+[.]+[com]$"

def func(m):
    if (re.finditer(regex,m)):
        print("new it is true","-----",m)
        
    else:
        print("false:---",m)
       
func(m)       


#############################


import re

no = (r'(\d{3}\W\d{3}\W\d{2}\W\d{2})')
f2 = open("G:\\Notepadd_python\\reg_pro.txt","r+")

#print(f2.readline())

for line in f2:
    out = re.findall(no,line)
                                                           #####VVVVIMP
    for i in out : 
        print(i)
              
        

print("________________________________")   



s="sivaramanatha@123hello"
 
r = re.findall('\d{3}',s)
print(r)      