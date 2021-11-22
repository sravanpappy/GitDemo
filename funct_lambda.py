
# def factorial(n):
	# if n==1:
		# result = 1
	# else:
		# result = n*factorial(n-1)
	# return result
# print(factorial(5))



# s=lambda n :n*n
# print(s(2))

# sum=lambda a,b:a+b
# print(sum(5,6))


# s=lambda a,b:a if a>b else b
# print(s(10,20))



##With out Lambda function

# def is_even(x):
    # if x % 2== 0:
        # return True
    # else:
        # return False

# l=[1,5,4,10,8,7,25,36,3]
# l1=list(filter(is_even, l))

# print(l1)        

##With Lambda Function   
# l2=list(filter(lambda x:x%2==0,l))
# print(l2)

# from functools import *
# ran=reduce(lambda a,b:a*b, range(1,10))
# print("This is rabge:",ran)


l=[0,5,4,8,15,7,33,50]
l1=list(map(lambda x:x*2,l))
print(l1)


data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
print("Original:",data_list)
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    


print ("After sorting:",new_list)

data = [-5, -23, 5, 0, 23, -6, 23, 67]
print(data.sort())
#print(a)


