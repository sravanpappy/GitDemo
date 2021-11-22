#### map() Function

####Without Lambda

# l=[1,2,3,4,5,6]
# def double(x):
	# return 2*x
# l1=list(map(double,l))
# print(l1)	


### With lambda function

# l2=list(map(lambda x:2*x,l))
# print(l2)


###sqaure of numbers 

# s=(1,2,3,4,5,55,4,8,77)
# l3=list(map(lambda x:x*x,s))
# l3=list(map(lambda x:x*x,s))
# print(l3)



# si1=[1,5,8,7]
# si2=[11,55,88,77]

# l4=list(map(lambda x,y : x*y,si1,si2))
# print(l4)


# s="sravan","pavan","Kumar"
# names=list(map(lambda x:x.capitalize,s))
# print(names)

# name11=list(map(lambda x:x.casefold, s))
# print(name11)

# d=lambda s:capitalize.s
# print(d)

# new=[11,2,5,8]
# sq=list(map(lambda x:2*x,new))

# print("nwew one is:",sq)


# n=[1,2,3,4,5]
# def given(x):
    # return x*x
# g=list(map(given,n))   
# print(g) 


#lambda x: True if x % 2 == 0 else False
m=[1,2,3,4,5,6,7,8,9]
s=list(map(lambda num:True if num%2==0  else False, m))
print(s)

new=list(filter(lambda x:x%2==0,m))
print("this one is even number:",new)
new1=list(filter(lambda x:x%2!=0,m))
print("this is nt equal:",new1)


f=list(filter(lambda x:x%2 ==0,m))
print("new:",f)
ff=list(filter(lambda x:x%2 !=0,m))
print("old:",ff)

y=[1,2,3,4,5,6,7,8,9]
d=list(map(lambda x: x*x,y))
print(d)

def fac(n):
    if n==0:
        result = 1
    else:
        result=n*fac(n-1)
    return result
print(fac(5))        