#### Decarators ###

def outer(func):
    def inner(a,b):
        print("the values are taken:",a,b)
        if b==0:
            print("this is not divided")
        else:
            return func(a,b)
    return inner



@outer
def division_1(a,b):
        return a/b
print(division_1(10,5))  



def up(func):
    def inner ():
        a=func()
        return a.upper()
    return inner

def sw(func):
        def inner():
            c=func()
            return c.title()
        return inner

def spli(func):
            def inner():
                d=func()
                return d.split()
            return inner


@spli
#@up
@sw
def new():
    return "hi this is new on eplese split it"
    
print(new())



      