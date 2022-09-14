n=1

while n<=100:
    c=1
    prim=0
    while c<=n:
        if n%c==0:
            prim+=1
        c=c+1
    if prim==2:
        print(n)
    n+=1
