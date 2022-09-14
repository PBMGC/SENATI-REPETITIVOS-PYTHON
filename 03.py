n=int(input("Numero:"))
divi=[]
divisores=0
for i in range(1,n+1):
    if  n%i==0:
        divisores+=1
        divi.append(i)
print("Tiene",divisores,"divisores")
print("Los divisores son",divi)