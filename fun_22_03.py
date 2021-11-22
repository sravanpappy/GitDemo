def funprracte(countryname): 
    if countryname == "india":
        return "new delhi"
    else:
        return "no Country"
print(funprracte("indi")) 


def new ():
    print("hello world")
new()    

def new1(country):
    if country !=  "india":
        return "Other Capital"
 
print(new1("indi"))  



def name (names1):
    print("hello",name,"good morning")
name("sravan")    

def square(number):
    print("the sqaure number",number,"is", number*number)

square(22)


def getmarks(a,b,**arg):
    for key, value in arg.items():
        print(%s==%s %(key,value))
getmarks("a":10,"b":20,30,40)        
        





   