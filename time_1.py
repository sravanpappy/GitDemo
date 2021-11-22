# import time
# x=time.strftime("%m%d%y")
# print(x)

# y="31 March 2021"
# s=time.strptime(y,"%d %B %Y")
# print(s)
# print(type(s))


# from datetime import datetime

# now= datetime.now()
# print("this is current date and time:", now)
# year=now.strftime("%y")
# print("this is year:", year)
# month=now.strftime("%M")
# print("Current month:",month)

# date=now.strftime("%d")
# print("Currrent Date:",date)

# time=now.strftime("%H:%M:%S")
# print("Time:",time)


# datetime=now.strftime("%y/%m/%d,%H:%M:%S")
# print(datetime)








from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)