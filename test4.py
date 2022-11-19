import re

w = "    .    "
literal = "5.5"

x = re.findall(r"-?[\d]+\.[\d]+", literal)

print(x)