n=int(input("Numero:"))
x=int(input("Tabla de:"))
y=int(input("hasta la:"))

for i in range(x,y+1):
    print(n,"*",i,"=",n*i)