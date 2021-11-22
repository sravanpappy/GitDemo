##### Decarator


# def outer(func):
    # def inner(name,lastname):
        # if name == "sravan":
            # print("HI sravan Good mornig")
        # else:
            # func(name,lastname)
    # return inner

# @outer

# def new (name,lastname):
        # print("hello", name,lastname,"Bad morning")
       
# new("ganga","pavan")

# #################################################
# def gst(func):
    # def inner(OP,NP):
        # if OP==0 and NP==0:
            # print("NOT Valid")
        # else:
            # func(OP,NP)
    # return inner

# @gst

# def gst1(OP,NP):
        # OP=int(input("Ente"))
        # NP=int(input("enter"))
        # GST_amount = NP-OP
        # GP=((GST_amount*100)/OP)
        # print("GST=",end=' ')
        # print(GP,end=' ')
        # print("%")
        # func(OP,NP)
# gst1(100,120)        
        
    

#################################################

# def gst1(func):
    # def inner(OP,NP):
        # OP=int(input("Ente"))
        # NP=int(input("enter"))
        # GST_amount = NP-OP
        # GP=((GST_amount*100)/OP)
        # print("GST=",end=' ')
        # print(GP,end=' ')
        # print("%")
    # return inner    
        
 
# @gst1


# def gst(OP,NP):
    # if OP==0 and NP==0:
        # print("NOT Valid")
    # else:
        # func(OP,NP)
      
# print(gst(0,0))
# a=10


def div(func):
    def inner(a,b):
        if b==0:
            print("This is not valid-------")
            return
        
        return func(a, b)
    return inner

@div
def cal(a,b):
    
    print(a/b)

cal(10,1)




