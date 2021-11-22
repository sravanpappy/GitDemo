

##### Exception handling

# try:
    # f=open('namesfile.txt',"r")
    # print(f.reads())
   
# except Exception as e:
    # print(e)
    #print("File is not found")
# finally:
    # print("exception to file")
        

f=open('namesfile11.txt',"a")
f.write("\n new data")
try:
    f=open('namesfile11.txt',"r")
    print(f.read())
        
except Exception as e:
    print(e)
    print("Exception is identified")
finally:
    print("file to exception")
   
# j=open('namesfile.txt',"r+")
# print(j.read()) 

# f=open('namesfile.txt',"r")
# print(f.read())



        