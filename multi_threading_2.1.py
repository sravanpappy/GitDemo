#######Multi threadig 


# from threading import * 
# import time 
# def display(): 
    # print(current_thread().getName(),"...started") 
    # time.sleep(3) 
    # print(current_thread().getName(),"...ended") 
# t1=Thread(target=display,name="ChildThread1") 
# t2=Thread(target=display,name="ChildThread2") 


# t1.start() 
# t2.start() 
# print(t1.name,"is Alive :",t1.isAlive()) 
# print(t2.name,"is Alive :",t2.isAlive()) 
# time.sleep(5) 
# print(t1.name,"is Alive :",t1.isAlive()) 
# print(t2.name,"is Alive :",t2.isAlive())


# num=int(input("Enter a number:")) 
# for i in range(1,num+1): 
    # print(" "*(i-1),end="") 
    # # for j in range(0,num+1-i): 
        # # print(2*num+1-2*i,end=" ") 
    # for k in range(1,num+1-i): 
        # print(2*num+1-2*i,end=" ") 
    # print() 
   
# import os
# try:
    # help(os)
    # print("Hissss")
   
# except Exception as e:
    # print(e)
   
# from random import *
# for i in range(10):
    # print(randint(1,100))
   
import os
# current_dir=os.getcwd()
# print(current_dir)   
# print(os.listdir('.'))
