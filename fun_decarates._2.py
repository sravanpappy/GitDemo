

def sw(func):

	def inside():
		new=func()
		return new.swapcase()
	return inside
    
def sp(fun):
        def innerd():
            new1=fun()
            return new1.split()
        return innerd
@sp         
@sw
def swap():
		return "Hi Thsi is sravan"
		
print(swap())		
		
        
        
def smart_division(func): 
    def inner(a,b): 
        print("We are dividing",a,"with",b) 
        if b==0: 
            print("OOPS...cannot divide") 
            return 
        else: 
            return func(a,b) 
    return inner 

@smart_division 
def division(a,b): 
    return a/b 
print(division(2,0))    
 
#print(division(20,2)) 
#print(division(20,0))        



def neww(func):
    def inh(a,b):
        print(a,"dividing by",b)
        if b==0:
            return "this is not divided"
        else:
            return func(a,b)
    return inh

@neww
def one(a,b):
    return (a/b)

print(one(1,5))    




















    
        