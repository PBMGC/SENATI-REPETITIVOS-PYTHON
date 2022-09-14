n=[]
np=0
ni=0
c=0
for i in range(1000,10000):
    np=0
    ni=0
    n1= i // 1000
    n2=( i % 1000 ) //100
    n3= ( ( i%1000 ) %100 ) //10
    n4= i % 10
    
    if n1%2==0:np=n1
    if n2%2==0:np=n2+np
    if n3%2==0:np=n3+np
    if n4%2==0:np=n4+np
    
    if n1%2==1:ni=n1
    if n2%2==1:ni=n2+ni
    if n3%2==1:ni=n3+ni
    if n4%2==1:ni=n4+ni

    if np==ni:
        n.append(i)
        np=0
        ni=0
    else:
        np=0
        ni=0
print("Numeros:")
print(n)