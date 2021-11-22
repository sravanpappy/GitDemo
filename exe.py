lst = ['sravn','kumar',['trilochan',['reddy'],['siva',['ram',['natha']]]]]

#output=['sravan kumar','trilochan reddy','siva ram natha']
# print(len(lst))

a=lst[0]
b=lst[1]
z= []
z.append(a)
z.append(b)
c =' '.join(z)
c.split()
d = []
d.append(c)
print(d)                           ###sravan kumar




#lst = ['sravn','kumar',['trilochan',['reddy'],['siva',['ram',['natha']]]]]
z=lst[2]
y=z[1]
x=z[0]
g=[]
g.append(x)
g.extend(y)
h=' '.join(g)
t1=list(h)
#print(t1)                       ###trilochan reddy



w=z[2]                      
aa=w[0]
#print(aa)                              ###siva


ab=w[1]                 
#print(ab)

abc=ab[0]
abd=ab[1]
a1=[]
a1.append(abc)
#print(a1)

abcd=[]
abcd.extend(a1)
#print(abcd)

abcd.extend(abd)
#print(abcd)

abcde=' '.join(abcd)
#print(abcde)                       ###ram natha



list=aa+abcde
#print(list)                    ###sivarama natha


d.append(h)
d.append(list)
print(d)

