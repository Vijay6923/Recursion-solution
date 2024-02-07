def string_length(s):
    
    if s == "":
        return 0
    
    else:
        return 1 + string_length(s[1:])

str = input("Enter a string: ")
ans=string_length(str)
print(ans)
