##instagram


###multiple assignment
a = [1,2,3]     #list
b = (4,5,6)     #tuple
c = {7,8,9}     #set

p,q,r = a
s,t,u = b 
w,x,z = c
print(a[::-1])
print(b)
print(c)


# Python program to Reverse each word of a string       ####   VVVV IMP   ##########    
# function definition
def reverseword(s):
  w = s.split(" ")
  # Splitting the string into a list of words# reversing each word and creating a new list of words
  nw = [i[::-1] for i in w]
  # Joining the new list of words to form a new string
  ns = " ".join(nw)
  return ns
  
# main() method
s = input("Enter the string: ")
print("return of the each word:", reverseword(s))



# import turtle
# colors = ['red', 'purple', 'blur', 'green', 'orange', 'yellow']
# t= turtle.pen()
# turtle.bgcolor('black')
# for x in range(360):
    # t.pencolor(colors[x%6])
    # t.width(x/100 + 1)
    # t.forward(x)
    # t.left(59)
# print(x)    



ac=round(20.5)
ab=round(19.5)
print(ac-ab)

