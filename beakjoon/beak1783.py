a,b = map(int, input().split())

if a==1:
    print("1")
elif a==2:
    print(min(4,(b+1)//2))
elif b<7:
    print(min(4,b))
else:
    print(b-2)
    
    
