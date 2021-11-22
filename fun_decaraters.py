def new():
    return "hi good morning"
print(new())

def str_upper(func):
        def inner():
            str1=func()
            return str1.upper()
        return inner

a=str_upper(new)
print(a())        


def new1():
    return "hi good morning"
def sw_str(func):
    def inner_s():
        new=func()
        return new.upper()
    return inner_s

swap=sw_str(new1)
print(swap()) 




def case_new(func):
    def old_fun():
        new=func()
        return new.swapcase()
    return old_fun

sw=case_new(new1)
print("hi this is swap case:",sw())    
        
        