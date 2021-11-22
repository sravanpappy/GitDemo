#def fun():
#   print("hello world")
#print("this:",fun())


# def abc(a):
    # print(a* 10)
# print(abc(5))


# def default(name='india'):
    # print(name)
# print(default())
# print(default("uk"))



# def ab(name='sravan'):
    # print(name)
# print(ab(['kumar']))


# def a ():
    # print("welcome")
# print("this is printes:",a())



# def abc (a):
    # print(a+10)
# print(abc(5))



# def para (parameter):
    # print(parameter+' kumar')         #####---pameterised function-----#####
# print(para('sravan')) 

# def non():
    # print("nonparameter function")         ###---non parameterised function####
# print(non())    


# def defl (name="sravan"):
    # print(name)                         ####-----default parameterised function#####
# print(defl("kumar"))


# x={"sravan","kumar","natha"}
# def getnames(li):                   #### --- pass list into a list,tupple,srting,set-----###
    # for x in li:
        # print(x)
# print(x)


# def tri(k):
  # if(k >0):
    # result = k + tri(k - 1)
    # print(result)
  # else:
    # result = 0
  # return result

# print("\n\nRecursion Example Results")
# tri(6)


# words = ['cat', 'window', 'defenestrate']
# for w in words:
    # print("name:",w, len(w))

# cat 3
# window 6
# defenestrate 12


# for i in range(5):
    # print(i)
    
    
# x = int(input("Please enter an integer:42 "))
#Please enter an integer: 42
# if x < 0:
     # x = 0
     # print('Negative changed to zero')
# elif x == 0:
     # print('Zero')
# elif x == 1:
     # print('Single')
# else:
     # print('More')
# y=x(42)
# print(y)

#a = ['Mary', 'had', 'a', 'little', 'lamb']
#for i in range(len(a)):
 #   print(i, a[i])
    
    
#a=['apple', 'banana', 'cat']

# for i in a:
    # print(i, len(i))
    
# print(range(10))
# range(0, 10)


# sum(range(5))


# for n in range(2, 10):
    # for x in range(2, n):
        # if n % x == 0:
             # print(n, 'equals', x, '*', n//x)
             # break
    # else:
         #loop fell through without finding a factor
         # print(n, 'is a prime number')
         
         

# x=["sravan',"pavan","kumar"]
# def getnames(li):
    # for x in li:
        # print(x)
        
# print(getnames())



# x=["sravan","kumar","natha"]
# def getnames(li):                   #### --- pass list into a list,tupple,srting,set-----###
    # or x in li:
      # print(x)
# print(getnames(x))

# sd=["a","c","b"]
# def naaa(list):
    # for sd in list:
        # print(sd)
# print(sd)
# print(naaa(sd))

# def sum(a,b):
    # c=a+b
    # return c
# s1=sum(10,20)
# print(s1)

# def getcountryname(countryname):
    # if countryname == "india":
        # return "newdelhi"
    # elif countryname == "usa":
        # print("washington")
    # else:
        # print("other_country")
# print(getcountryname("usa"))


# def browsername (browser):
    # if browser == 'chrome':
        # print("print google chrome")
    # elif browser == 'firefox':
        # print ("launch firefox")
    # else:
        # print("other")
# print(browsername("chrome"))


# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

#ach function call represents an elf doing his work#
# def deliver_presents_recursively(houses):
   #Worker elf doing his work
    # if len(houses) == 1:
        # house = houses[0]
        # print("Delivering presents to", house)

   #Manager elf doing his work
    # else:
        # mid = len(houses) // 2
        # first_half = houses[:mid]
        # second_half = houses[mid:]

       # Divides his work among two elves
        # deliver_presents_recursively(first_half)
        # deliver_presents_recursively(second_half)
# print(deliver_presents_recursively("Eric's"))



# def fact(num):
    # if (num>1):
        # num = num*fact(num-1)
        # return num
# print(fact(5))

# def login (username, password):
    # print(username, password)
# print(login(username="sravan", password="india@123"))  

# def getmarks(*arg):
    # for i in arg:
        # print(i)
# print(getmarks(10,20,40,15,12))

# def names(*name):
    # for namess in name:
        # print(namess)
# print(names('sravan', 'kumar'))


# def keyva (**args):
    # for key, value in args.items():
    # print(%s==%s %(key, values))
# print(keyva(sravan= '23'))

# def sum(arg1, arg2):
    # total=arg1+arg2
    # print ("total function:", total)    
    # return total
# print(sum(10.525888,20.0001))  

# def namel(*names):
    # for k in names:
        # print(k)
# print(namel(["sravan", "kumar","pavan","kumar"]))

# def city(**names):
    # for key, value in names.items():
        # print("%s= %s" %(key,value))
# print(city(name=10,age=23,names='sravan',hjj='loni'))


# def froots(**names):
    # for key,value in names.items():
        # print("%s=%s" %(key, value))
# print(froots(green='apple', orange='banana',red='dragonfroot'))

# cube = lambda x:x/x-x
# print(cube(5))


#######################Sivaram##############################

##Requred argument##


def namess(a,b):
    print(a)
    print(b)
    print(a+' '+b)
    
namess("sravan","kumar")

def add(a,b):
    print (a+b)
add(10,5)

def total(a,b,c):
    print(a+b-c)
total(10,20,20)


###  2  default argument #########

def names (a,b,c=45):
    print(a+b+c)
names(10,20)

# def pracice(a=8,b=8,c):
    # print(a+b+c)                          ###not valid
# pracice(2)

#### key word length argument ######

def keyw (a,b,c):
    print (a)
    print (b)
    print (c)
keyw(5,10,15)


def lenth (a,b,c,g):
    print(a)
    print(a-b)
    print(c-a)
    print(a+b+c+g)
    
lenth(10,5,2,3)


##################### varibale lenth argument #############3

def var(a,b,c,*d):
    print ("a value", a)
    print ("b value", b)
    print ("c value", c)
    for i in d:
        print(i)
var(20,30,40,50,60,80,90,100)


#####          key word variable argument ############
def key (**b):
    print(b)

key (age=20, name= 'trilochan', cource='python')




# def ma(list):
    # if list == "malayalam"
    
    


# a="malayalama"
# def name(a):
    # return a == a[::-1]
# out = name(a)
# if out:
    # print("Yes")
# else:
    # print("No")
    
       
m="malayalamm"
mm=m[::-1]
if m==mm:
    print("this is palndrom:",m,":", "yes")
else:
    print("this not palndrom:",m,":", "no")



# def sr(m):
    # return m == m[::-1]
# if sr==m:
    # print ("yes")
# else:
    # print("no")
    

   




# l="malayalam"
# ll=[::-1]
# def get(ll):
    # if l == l[::-1]
        # print("This is palndrom:", "yes")
    # else:
        # print("This is not palandrome:", "no")


    













