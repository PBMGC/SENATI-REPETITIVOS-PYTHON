n=[]
c=0
for i in range(100,1000): 
   p1=i//100
   p2=i%10

   if p1==p2:
    c+=1
    n.append(i)
print("Hay",c,"Numeros Capicua")
print(n)