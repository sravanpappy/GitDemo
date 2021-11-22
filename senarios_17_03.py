mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)



lis=[22,31,45,49,22,49,60,89,60,71,31]
lis=list(dict.fromkeys(lis))
print(lis)


lis1 = list(set(lis))
print(lis1)

lis2=[22,31,45,49,22,49,60,89,60,71,31]

res = [] 
for i in lis2: 
    if i not in res: 
        res.append(i)
        
print(res)





lis=[22,31,45,49,22,49,60,89,60,71,31]
# lis1 = list(set(lis))
# print(lis1)
# lis2=list(dict.fromkeys(lis))
# print(lis2)



my_list = [1,1,2,3,2,2,4,5,6,2,1]
my_final_list = set(my_list)
print(list(my_final_list))

###############3

