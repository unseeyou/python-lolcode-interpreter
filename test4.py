# import re

# w = "    .    "
# literal = "5.5"

# x = re.findall(r"-?[\d]+\.[\d]+", literal)

# print(x)


x = [1,2,3,4,5]

for i in x:
    print(i)
    x.remove(2)
    x.remove(3)
    x.remove(4)
    x.remove(5)