###senarios######

# f=open("senarios","w")
# f.write("["sravan","pavan","kiran","siva","ram"]")
# f=open(senarios","r")
# print(f.read())

# names=["sravan","pavan","kiran","siva","ram"]

f = open("namesfile", "w")
f.write("'ravan','kiran','pavan','sivaram'")

f = open("namesfile", "r")
print(f.read())

newlist=[x for x in f if x]
#print(newlist)
#print(len(newlist))
newlist1=str(newlist)
print(newlist1)

#print(my_list)
#print(len(my_list))
#print(my_list[-1])
#print(my_list[index])