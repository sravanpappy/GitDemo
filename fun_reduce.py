numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
   product *= num

print(product)

a=[1,2,3,4,5,6,7,8,9]
b=1
for num in a:
    b=b*num
print(b)
 
aa=[1,2,3,4,5,6,7,8,9]
from functools import reduce 
l=reduce(lambda x,y:x*y,aa)
print("this is using lambda function:",l)  



aa=[1,2,3,4,5,6,7,8,9]
def f(a,b):
    return a if a>b else b
print(f) 





min_f=[55,4,3,66,7,2,98,0]
#from functools import reduce 
lam=reduce(lambda x,y:x if x>y else y,min_f)
print("hey i am using lambda:this is bigg numabr:",lam)

lam_s=reduce(lambda a,b:a if a<b else b, min_f)
print(lam_s)

min(min_f)
print("this is shrt:",min_f)


ran=reduce(lambda a,b:a+b, range(1,10))
print("This is rabge:",ran)


# def a(name):
    # print("hellow name:",name)
#a("sravan") 

# aa=a
# aa("sravan") 
# del(a) 
# a("sravan") 


z=[1,22,4,5,8,4,99]
from functools import *
new=reduce(lambda a,b:a if a>b else b,z)
print("hi This is new one:",new)

low=reduce(lambda x,y:x if x<y else y,z)
print("low:",low)