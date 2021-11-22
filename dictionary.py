#data={1:"sravan", 2:"pavan", 4:"natha"}
#print(data)
#print(data[1])
#print(data[3])
#print(data.get(3,"not defined"))
#print(data.get(1,'not define'))

# a=[1,2,3,5,]
# b=['s','b','c','g']

# c=dict(zip(a,b))
# print(c)
# print(c.get(1))

#aa={8:['a','b'], 8:"sravan", 8:{'ab':"natha", 'ac':"trilochan"}}
#print(aa)
#print(aa.get(8,"not defined"))
#print(aa[8])
#print(dir(dict))


#ini_dict = {'nikhil': 1, 'vashu' : 5, 'manjeet' : 10, 'akshat' : 15} 
  
# printing initial json 
#print ("initial 1st dictionary", ini_dict) 
  
# changing keys of dictionary 
#ini_dict['akash'] = ini_dict.pop('akshat') 
  
# printing final result 
#print ("final dictionary", str(ini_dict))


#ab={'a':"apple", 'b':"banana", 'c':"cat"}
#print(ab)
#ab['z']=ab.pop('b')
#print(ab)
#print(dir(dict))

#s="sravan kumar"
#sd=s.split("")
#print(sd)

# def multiplyList(myList) :
    # result = 1
    # for x in myList:
         # result = result * x 
    # return result

#s=[1,2,3]
#t=(9,10)

#s+=t
#print("the values:",s)
#op=[(1,1),(2,8),(3,27)]

#ss=[sk * 3 for sk in s]
#print("some data prined:",ss)

#cubes= list(map(lambda x: x ** 3, s))
#print(cubes)

#d=dict(zip(s,cubes))
#print(d)

######################################################


#l=[1, 2, 3]
#t=('kiran', 'pavan', 'sravan')    ###any to list convert#####
#l+=t
#print(l)

            ###################
            
# t_list=[1,2,3,4]
# t_tuple=(9,10)
# res=tuple(list(t_tuple)+t_list)
# print(res)


# l=["sravan", "kumar"]
# s={1,2,3}
# c=tuple(list(s)+l)
# print("concatinare of set and list in to 'tuplele':",c)

# ab=[1,2,3]
# aa={1:"sravan", 2:"kumar", 'ravi':1}
# ab+=aa
# print(ab)


# list1 = [1, 2, 5, 6] 
# res = [(val, pow(val, 3)) for val in list1] 
# print(res)





# s={1:'a', 2:'b', 3:'c'}
# print(s.clear())
# print(s)

#sd={1:'kumar', 2:'kumar', 3:'ram'}
#e=sd.copy()
#print("it will display:",e.fromkeys(sd,5))


#seq = { 'a', 'b', 'c', 'd', 'e' } 
#res_dict = dict.fromkeys(seq)

#print ("The newly created dict with None values : " + str(res_dict))

#res_dict2 = dict.fromkeys(seq, 1) 

#print ("The newly created dict with 1 as value : " + str(res_dict2))


#car = {"brand": "Ford", "model": "Mustang", "year": 1964}

#x = car.get("model")

#print("model is printed:",x)

#print(dir(dict))

#print(car.popitem())
#print(car)


#cubes= list(map(lambda x: x ** 3, s))
#print(cubes)


# s=(1,2,3,4,5,5)
# c=list(map(lambda x: x ** 4, s))
# print(c)

# a={1:'a',2:'b',3:'f'}
# b=a.setdefault(3,'c')
# print(b)

# car = {
  # "brand": "Ford",
  # "model": "Mustang",
  # "year": 1964
# }

# x = car.setdefault("model", "Bronco")

# print(x)

# sd={"name":"sravan","surname":"g"}
# sd.update({"phno":964000366})
#print(sd)
# print(sd.values())



data={'names':['sravan','trilochan','sivaram'],'education':"'mba','msc','btech'",'village':{"tadipatri","cherlopalli","boppepalli"}}

a= [data['names'][0]]
b=[data['education'][1:4]]
cc=data.get('village')
change=list(cc)
c=[change[0]]
a.extend(b)
a.extend(c)

aa=data.keys() 
print(aa)
print(a)              
final=dict(zip(aa,a))
print(final)



#################################


v='sravan'
m='kumar'
l='ganga'
kk=v,m,l
print("thia is printed:",list(kk))









#print(cc)
#c=[data['village']index(0)]
#print(len(data))





