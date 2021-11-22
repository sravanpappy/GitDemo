import re

# no = (r'(\d{1,3}\.\d{1,3}\.\w{2}\.\w{2})')
f2 = open("G:\\Notepadd_python\\reg_pro.txt","r+")
# #print(f2.readline())


# k = re.compile('\d{0,2}.\d{..}\W.\d{.}\W.\d{.}',f2)
# print(k)
# # for line in f2:
    # #out = re.findall(no,line)
                                                            # #####VVVVIMP
    # #for i in out : 
        # #print(i)
    # #print(out)       
        


new = re.findall(r'(\d{1,3}\.\d{1,3}\.\w{2}\.\w{2})',f2)
print("________________________________",new)


#no = (r'(\d{1,3}\.\d{1,3}\.\w{2}\.\w{2})')

# noo = (r'(\d{1,3}\.\d{1,3}\.\d[0-2]\.\d[0-2])')
# f22 = open("G:\\Notepadd_python\\reg_pro.txt","r+")

# for line in f22:
    # out = re.findall(noo,line)
    # for i in out : 
        # print(i)
    # print(out)       
               
        
# s=input("enter ur name")
# m=re.search(s,"ababababaabab")
# if m != None:
    # print("match is avalable")
    # print(m.start(),"----",m.end(),"---",m.group())
   
# else:
    # print("string is not matched")
   
# text = "To email Guido, try guido@python.org or the older address guido@google.com."
# email.findall(text)

s="sivaramanatha123hello"
 
r = re.findall('\d..',s)
print(r)