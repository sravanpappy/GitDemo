##########Multi threading part 2
# from threading import *
# from time import *

# class name:
    # def m1():
        # for i in range (10):
            # print("Hi this is inner class")
            # sleep(1)
           
# class last:
    # def m2():
        # for i in range (10):
            # print("This is inner class")
            # sleep(1)
                   
# t1=Thread(target=name.m1)
# t2=Thread(target=last.m2) 
# t1.start()
# t1.join()
# t2.start() 

from threading import *
import time
def double(numbers):
    for n in numbers:
        time.sleep(.05)
        print("Double value:",2*n)
       
def squares (numbers):
    for n in numbers:
        time.sleep(.05)
        print("Sqare numbers:",n*n)
       
numbers=[1,2,3,4,5,6,7,89,25.2,45,58,3.33]
begintime=time.time()
t1=Thread(target=double, args=(numbers,))
t2=Thread(target=squares, args=(numbers,))
t1.start()
t1.name="Sravankumar"

t2.start()
t1.join()
t2.join()


endtime=time.time()
print("Total Time:",endtime-begintime)

print("*"*20)
from threading import *
print(current_thread().getName())
current_thread().setName("sravan")
print(current_thread().getName())


print("*"*25)

import time

def test():
    print("Child Thread")
   
t=Thread(target=test)
t.start()

print("The main identification number:",current_thread().ident) 
print("The main CHILD number:",t.ident) 
print("The number:",current_thread().getName())   
       
print("*"*30)


def dis():
    print(current_thread().name,"--------started")
    time.sleep(3)
    print(current_thread().name,"ended ------")
   
print("The no of active threads:",active_count())


t1=Thread(target=dis,name="Child thread ------1")
t2=Thread(target=dis,name="Child thread ------2")  
t3=Thread(target=dis,name="Child thread ------3") 
t1.start()
t2.start()
t3.start()
print("The no of active threads:",active_count())
time.sleep(3)
print("The no of active threads:",active_count())
time.sleep(2)
print("The no of active threads:",active_count())
 
 

print("*@"*30)


def dis():
    print(current_thread().name,"--------started")
    time.sleep(3)
    print(current_thread().name,"ended ------")
   
print("The no of active threads:",active_count())


t1=Thread(target=dis,name="Child thread ------1")
t2=Thread(target=dis,name="Child thread ------2")  
t3=Thread(target=dis,name="Child thread ------3") 
t1.start()
t2.start()
t3.start()

l=enumerate()
for t in l:
    print("Thread name:",t.name)
    print("Identification number:",t.ident)
    print() 
   
time.sleep(5)
l=enumerate()
for t in l:
    print("Thread name:",t.name)
    print("Identification number:",t.ident)
    print()
   
# print("The no of active threads:",active_count())
# time.sleep(3)
# print("The no of active threads:",active_count())
# time.sleep(2)
# print("The no of active threads:",active_count())
  
           
           
 

                                
    