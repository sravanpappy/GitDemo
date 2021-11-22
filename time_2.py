


from datetime import datetime 

now=datetime.now()

j=now.strftime("%Y-%B-%d %H:%M:%S")
print(j)
k=now.strftime("%Y-%m-%d %H:%M:%S")
print(k)
l=now.strftime("%Y/%b/%A %H:%M:%S")
print(l)

today = datetime.today()
print(today)


m=today.strftime("%Y-%m-%d %H:%M:%S")
print(m)

n=today.strftime("%Y-%m-%d %H:%M:%S.%f")

print(n)