###generators


#x=[x*x for x in range(100000000000000000000000000000000)]
#print(x)       ####It throws memory error


import time
def countdown(num):
    print("count down started ..........")
    while num >0:
        yield num
        num=num-1
    else:
        print("Lets go")
        
values = countdown(2)
for x in values:
            print(x)
            time.sleep(1)

## to generate first n number


def first(num):
    n=1
    while n <= num:
        yield n
        n=n+1

for x in first(2):
            print(x)
            time.sleep(1)
            
   
### Fibonacci numbers

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
for n in fib():
            if n>100:
                break
            print(n)    
print(type(countdown))            