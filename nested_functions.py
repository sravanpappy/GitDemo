# def outer(): 
    # print("outer function started") 
    # def inner(): 
        # print("inner function execution") 
    # print("outer function calling inner function") 
    # inner() 
   
# outer()

# def outer(): 
    # print("outer function started") 
    # def inner(): 
        # print("inner function execution") 
    # print("outer function calling inner function") 
    # return inner
    
# f=outer
# print(f)
# f()

# def outer(): 
    # print("outer function started") 
    # def inner(): 
        # print("inner function execution") 
        # def ininner():
            # print("inner and inne")
        # return ininner    
    # print("outer function calling inner function") 
    # return inner
   
# f=outer()
# g=f()
# g()



# def outer(): 
    # print("outer function started") 
    # def inner(): 
        # print("inner function execution") 
        # def ininner():
            # print("inner and inne")
        # return ininner ()   
    # print("outer function calling inner function") 
    # return inner
   
# outer()




# def decor(func): 
# def inner(name): 
# if name=="Sunny": 
# print("Hello Sunny Bad Morning") 
# else: 
# func(name) 
# return inner 
 
# def wish(name): 
# print("Hello",name,"Good Morning") 
 
# decorfunction=decor(wish) 

# wish("Durga") #decorator wont be executed 
# wish("Sunny") #decorator wont be executed 
 
# decorfunction("Durga")#decorator will be executed 
# decorfunction("Sunny")#decorator will be executed 



a=[1,22,1,22,4,55,5,55]
aa=set(a)
print(aa)
