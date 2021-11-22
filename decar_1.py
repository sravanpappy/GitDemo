###### Deacartor_senarios
   


def add(func):
    def inner(a, b):
        return(a+b)                              ################
    return inner


@add
def new(a, b):
    return 
   
print(new(100,20))   






# def add(func):
    # def inner(a, b):
        # return func(a, b)#################20

    # return inner


# @add
# def new(a, b):
    # return a+b
   
# print(new(100,20))   



# def inc(x):
    # return x + 20
    
# def operate(func, x):
    # result = func(x)
    # return result
   
# print(operate(inc,100)) 



def add(x):
    return (x + 20)
    
@add
def new_add(func, x):
        result=func(x)
        return result
print(new_add(add, 100))        




       
def servecetax (func):
        
        def inner():
            amt=func()
            newamt=amt+amt*0.0125
            return newamt
        return inner

@servecetax

def customer():
        return 100
       

final_amt=customer()
print(final_amt) 