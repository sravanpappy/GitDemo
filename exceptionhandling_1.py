
# try:
    # num = int(input("Enter a number: "))
    # assert num % 2 == 0
# except:
    # print("Not an even number!")
# else:
    # reciprocal = 1/num
    # print(reciprocal)
    
# try:  
  # print(x)
# except:
  # print("An exception occurred")    
  
  
  
  
#try:
 # print(x)
#except NameError:
 # print("Variable x is not defined")
# except:
  # print("Something else went wrong")  
  
  
  

# try:
  # print("Hello")
# except:
  # print("Something went wrong")
# else:
  # print("Nothing went wrong")


# x = "hello"

# if not type(x) is int:
  # raise TypeError("Only integers are allowed")  
  
  
  
  
# try:
    # print('try block')
    # x=int(input('Enter a number: '))
    # y=int(input('Enter another number: '))
    # z=x/y
# except Exception:
    # print("except ZeroDivisionError block")
    # print(Exception)
# else:
    # print("else block")
    # print("Division = ", z)
# finally:
    # print("finally block")
    
# print ("Out of try, except, else and finally blocks." )  



#!/usr/bin/python
try:
    def KelvinToFahrenheit(Temperature):
       assert (Temperature >= 0),"Colder than absolute zero!"
       return ((Temperature-273)*1.8)+32
    print (KelvinToFahrenheit(273))
    print (int(KelvinToFahrenheit(505.78)))
    print (KelvinToFahrenheit(-5))
except:
    print("this is error")
else:
        print("else part")
finally:
    print("final one")