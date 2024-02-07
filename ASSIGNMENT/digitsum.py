def dig_sum(x):
    if x==0:
        return 0
    else:
        return (x%10)+ dig_sum(x//10)

n=int(input("enter the number: "))
ans=dig_sum(n)
print(ans)