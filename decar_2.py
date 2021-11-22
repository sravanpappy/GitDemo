

# def add(func):
    # def file_xl_creationer(a, b):
        # return(a+b)                              ################
    # return file_xl_creationer

# @add
# def new(a, b):
    # return 
   
# print(new(100,20)) 

#################################################

# def inc(x):
    # return x + 20
    
# def operate(func, x):
    # result = func(x)
    # return result
   
# print(operate(inc,100)) 

##################################


# def adding(func):
    # def inner(a, b=20):
        # return a+b  
    # return inner
        
# @adding         
# def f_adding(a,b):
          # return   
         
# print("This is final output:-",f_adding(100))



###################################

def add(func):

    def inner():
        cal=func()
        calculation=cal+cal*0.175                  ##### Senario Exeample
        return calculation
    return inner

@add
def final():
       return 100
       
finalamout=final()
print(finalamout)     
        
        
        
       

