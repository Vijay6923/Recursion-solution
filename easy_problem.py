n=int(input())
q=list(map(int,input().split( )))
check=False
for i in q:
    if(i==1):
        check=True
        break
if(check):
    print("hard")
else:
    print("easy")
    