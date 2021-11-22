import re
# name="sivaramanatha"
# find_a=re.search("[^b-z]",name,3)
# print("Name of the word",find_a.start(),"----",find_a.group())




print("___________________________")

count=0
pname=re.finditer("a","sivaramanatha")
for i in pname:
    count+=1
    print(i.start(),"------",i.end(),"----",i.group())
   
print(count)   




print("___________________________")
  
import re

list = ["guru99 get", "guru99 give", "guru Selenium"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))
    
patterns = ['software testing', 'guru99']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print(email)




# txt = "sivaramanatha"
# x = re.finditer("[a]", txt, 2)

# print(x)
# for i in x:
    # print(i.start(),"--",i.end(),"--",i.group())
  


#############################################33  
   
# txt = "The rain in Spain"
# x = re.find(r"[a]", "9", txt)
# print(x)   


# txt = "sivaramanatha@123"
# x = re.search("a", txt)
# print(x) #this will print an object

import re

no = (r'(\d{1,3}\.\d{1,3}\.\d{2}\.\d{2})')
f2 = open("G:\\Notepadd_python\\reg_pro.txt","r+")

#print(f2.readline())

for line in f2:
    out = re.findall(no,line)
                                                            #####VVVVIMP
    for i in out : 
        print(i)
    #print(out)       
        

print("________________________________")




