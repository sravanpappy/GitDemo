sd=[1,2,34,5,86,98,1,2,5,2,5]
print(sd)

s=(123,458,698,1,25,25)
print(s)

set1={123,458,698,1,2,25,25}
print(set1)

set2={1,2,3,6,8,4,10,10}
print(set2)

###converctions####

## list to set
d=set(sd)
print("list to set  : ",d)


###set to list
set3=list(set2)
print("set to list  : ",set3)


#### touple to set
e=set(s)
print("touple to set  : ",e)

###set to tupple##
f=tuple(set2)
print("set to tupple   : ",f)

##list to tupple##
tu=tuple(sd)
print("list to tupple   : ",tu)

##tuple to list##
l1=list(s)
print("tuple to list   : ",l1)


#how to add element in string
ext=["sravan"]
exten=ext.extend("kumar")
print(exten)

