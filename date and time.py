from datetime import datetime
#
# print(datetime.now())
# print(datetime.today())
# v=datetime.today()
# print(v.year)
# print(v.month)
# print(v.date())
# print(v.hour)
# print(v.second)





now = datetime.now()
print(now)

year=now.strftime("%Y")
print(year)
month=now.strftime("%z")
print(month)

import time
print(time.gmtime())

# import os
# print(os.listdir())
#
# print(os.getcwd())
