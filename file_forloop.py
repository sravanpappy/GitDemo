# f = open("namesfile", "w")
# f.write("ravan,kiran,pavan,sivaram")

f = open("namesfile", "r")
f.readlines()
#print(f)
f1=list(f)
print(f1)

fh=[x for x in f if "sravan" in x]
# f

# for index in range(len(newlist1)):
    # print(newlist1[index])

# print(len(newlist1))





#for index in newlist1('pavan'):
#    print(newlist1[index])

#print(newlist1)
