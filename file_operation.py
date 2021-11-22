file = open('namesfile.txt',"r+")
#file.read()
print(file.readline(50))
#print(file.readlines())


new=[x for x in file if "pavan" in x]
print(new)

# for f in file:
    # if f !="sivaram":
        # print(f)
    
# print(f)

