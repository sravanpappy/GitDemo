list1 = [11,23,45,23,64,22,15,24]
#list comprehension
even_nos = [num for num in list1 if num % 2 == 0]
#print("Even numbers : ", even_nos)prine=[1,2,3,4,5,6,7,8,9,10,15,14,18,55,88]

ev=[v for v in prine if v % 2==0]
#print("even numbers printe:",ev)
od=[o for o in prine if o % 2!=0]
#print("odd numbers:",od)


new=[n for n in range (50) if all(n % y !=0 for y in range(2,n))]
print(new)



odd_num = [odd for odd in list1 if odd % 2 != 0]
#print("odd numbers:",odd_num)	
		
        
prime_num=[x for x in range(2, 40) if all(x % y != 0 for y in range(2, x))]

print("prime_num:",prime_num  )     


#even=[e for e in range(50) if e % 2!=0]
#print(even)




