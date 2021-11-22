
##### Regular Expression

import re
# count=0

# name=re.finditer("ab","abaababa")
# for i in name:
    # count+=1
    # print("index:",i.start())
   
# print("no of count:",count)  


# count=0
# new_one=re.finditer("ab","abababaabbababa")
# for i in new_one:
    # count+=1
    # print("start:{},end:{},group:{}".format(i.start(),i.end(),i.group()))
    # print("Index of each on:",i.start())
   
# print(count)  

count=0
new=re.finditer('[^ab]',"ababab@34abana")
print(type(new))
for i in new:
   # print(i.start(),"====",i.end(),"===",i.group())
    print(i.start(),"===",i.group())

