import re
def validRE(pattern, string_input):
    x = re.match(pattern, string_input)
    if(x):
        return True
    else:
        return False



print(validRE("^[A-Za-z]+[\w]*$", "1aruh"))





