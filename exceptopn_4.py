#(x,y) = (5,0.1)
#try:
  #  z = x/y
 #   print(z)
#except ZeroDivisionError as e:
	#z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
	#print (z)
    
 


 
# class B(Exception):
    # pass

# class C(B):
    # pass

# class D(C):
    # pass

# for cls in [B, C, D]:
    # try:
        # raise cls()
    # except D:
        # print("D1")
    # except C:
        # print("C2")
    # except B:
        # print("B3")
        
        
# try:  
    # a = [1, 2, 3] 
    # b= ("sravan","kiran")
    # print(b[0])    
    # print (a[0])  
# except LookupError:  
    # print ("Index out of bound error.") 
# else:  
    # print ("Success") 
    
    


# def my_generator(): 
    # try: 
        # for i in range(5): 
            # print ('Yielding', i) 
            # yield i 
    # except GeneratorExit: 
        # print ('Exiting early') 
  
# g = my_generator() 
# print (g.next()) 
# g.close()   
        
        
        
import sys 

#print ('Regular integer: (maxint=%s)' % sys.maxint) 
try: 
	i = sys.maxint ** 3
	print ('No overflow for ', type(i), 'i =', i) 
except OverflowError as err: 
	print ('Overflowed at ', i, err) 

print() 
print ('Long integer:') 
for i in range(0, 100, 10): 
	print ('%2d' % i, 2 ** i) 

print() 
print ('Floating point values:') 
try: 
	f = 2.0**i 
	for i in range(100): 
		print (i, f) 
		f = f ** 2
except OverflowError as err: 
	print ('Overflowed after ', f, err) 

        