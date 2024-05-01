# cook your dish here
t=int(input())
for _ in range(t):
    h, x, y=map(int,input().split())
    print(1+(int)((h-y+x-1)/x))