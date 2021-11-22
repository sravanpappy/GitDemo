##########Multi Threading


# import threading
# print(threading.current_thread().get_Nmae())

# from threading import *
# def display():
    # # for i in range (10):
        # print("Child thread name",current_thread().getNmae())
       
# t=Thread(target=display)
# t.start

# print("the main thread name :",current_thread().getNmae())


# from threading import *
# class Mythread(Thread):
        # def run(self):
            # for i in range(10):
                # print("Child thread is prenting")
               
# t=Mythread()               
# t.start()
# for i in range(5):
    # print("Mani thread")
    
   

# def new():
    # print("Child Thread:",current_thread().getNmae())
   
# a=Thread(target=new)  
# a.start() 

# from threading import *
# class property:
    # def p(self):
        # print("land+gold+money")
    # def marry(self):
        # print("aaaah")
         
# class son(property):
    # pass
        # # def marry(self):
            # # print("chhhhhhha")
           
# c=son()
# # c.p()
# # c.marry()           
# one=Thread(target=c)
# one.start()


from threading import *
from time import *
class name (Thread):
    def run(self):
        for i in range (50):
            print("This is one")
            #sleep(0.1)
           

class last(Thread):
    def run(self):
        for i in range(50):
            print("Second one")
            print("Active Threadss Find:",active_count())
            #sleep(0.1)
t=name()
tt=last()
t.start()
tt.start()
t.join()
tt.join()
print("Active Threadss Find:",active_count())   
for i in range(5):
    print("HIIIIIIIIIIIIIIIIIIIIII") 
    sleep(1)
    print("Active Threadss Find:",active_count())    


           
           
        