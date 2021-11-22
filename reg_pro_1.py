

#### Reg Expression Programs IQS

#file=open("G:\\Notepadd_python\\reg_pro.txt", "r+")
#print(new.open())

#import re
#new=re.finditer("[\w\W]","file")

# count=0
# result1=re.compile("[^a-zA-Z]")
# result = result1.finditer("G:\\Notepadd_python\\reg_pro.txt" )
# for i in result:
    # count+=1
    # print("start:{},end:{},group:{}".format(i.start(),i.end(),i.group()))
   
# print("the no of counters:",count)




###################


# count=0
# #result1=re.compile("r[a-zA-Z0-9]")
# result = re.finditer(r"[^a-zA-Z][0-20-20-10]","sravankumarsivaramanathaifwewatntorepresentdata123.253.14.2datato1454.2587.25thisissenari" )
# for i in result:
    # count+=1
    # print(i.start(),"----",i.group())
   
# print("the no of counters:",count)   




########################
# text = "sravankumarsivaramanathaifwewatntorepresentdata123.253.14.22datato,1454.2587.25thisissenari"
# result = re.sub(r"[a-z]", "", text)
# print(result)

#######################




# pattern = re.compile("r'(\d{1,3}\.\d{1,3}\.\d{1,2}\.\d{1,2})'")

# for i, line in enumerate(open('G:\\Notepadd_python\\reg_pro.txt')):
    # for match in re.finditer(pattern, line):
        # print ('Found on line %s: %s' % (i+1, match.group()))
        
        
       
################################

import re
fh= open("G:\\Notepadd_python\\reg_pro.txt","r+")


pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,2}\.\d{1,2})')

for line in fh:
    out=
###################
# import re

# no = (r'(\d{1,3}\.\d{1,3}\.\d{1,2}\.\d{1,2})')
# f2 = open("G:\\Notepadd_python\\reg_pro.txt","r+")
# #print(f2.readline())

# for line in f2:
    # out = re.findall(no,line)
    # # for i in out : 
        # # print(i)
    # print(out)  