

# from module_11 import f1

# f1()

from math import *
print("This is sqrt:25:",sqrt(25))
print("this is ceil:10.1:",ceil(10.1))
print("This is floor:10.1:",floor(10.1))
print("This is fabs:-10.6:",fabs(-10.6))
print("This is fabs:10.6:",fabs(10.6))
print("This islogs:1:",log(1))
print("This is sin:25:",sin(25))
print("This i tan:25:",tan(25))

# import math 
# help(math)


from random import * 
for i in range(10): 
    print(random())
    
    
    
import time
seconds = time.time()
print("Seconds since epoch =", seconds)



import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)	    