n = int(input()) 
d = list(map(int, input().split()))  
a, b = map(int, input().split())  


total_years = sum(d[a-1:b-1])

print(total_years)
