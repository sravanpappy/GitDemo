############ Regular Expressions


import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# print(x)

# txt1 = "The rain in Spain"
# x1 = re.split("\s", txt1)
# print(x1)

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)


# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# new= "The rain in Spain"
# new_one= re.sub("\s", "9",new, 2)
# print(new_one)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

