def reverse_string(str):
    if (len(str)== 1 or len(str)==" "):
        return str
    else:
        return str[-1] + reverse_string(str[:-1])

str= input("Enter a string: ")
ans=reverse_string(str)
print(ans)
