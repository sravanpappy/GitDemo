
# a=int(input("Enter Original Price:-"))
# b=int(input("Enter Net Price:-")

# def gst(func):

    # def new_gst(n):
       
        # OP = int(input("Enter Original Price:-"))
        # NP = int(input("Enter Net Price:-")
        # GST_amount = NP-OP
        
        # GP=((GST_amount*100)/OP)
        # print("GST=",end=' ')
        
        # print(round(GP),end=' ')
        # print("%")
        # return func(a,b)
        
        
    # return new_gst
# print(newgst1())  


# def gst():
    
    # def new_gst(): 
        
        # OP = int(input("Enter Original price:-"))
        # NP = int(input("enter Net Price:-"))
        # GST_amount = NP - OP

        # GP = ((GST_amount * 100) / OP)
        # print("GST = ",end='') 
          
        # print(round(GP),end='') 
        # print("%")
        
    # return new_gst() 
# print(gst())

  





def star(func):
    def inner(ar,kw):
        print("*" * 30)
        func(ar,kw)
        print("*" * 30)
    return inner


def percent(func):
    def inner(ar, kw):
        print("%" * 30)
        func(ar, kw)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg.zfill(20))

print("Hello")

def fu(func):

    def inner():
        func=cal
        cal_final=cal+cal*0.11
        return cal_final
                
    return inner

# @function

def new_f():
    return 100
       
print(new_f())
       
def f_name(func):

    def inner():
        cal=func()
        amt_f=cal+cal*0.25
        return amt_f
    return inner

@f_name
def new_name():
        return 100
       
print(new_name())       
     
     
    
