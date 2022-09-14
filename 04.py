n=int(input("Numero:"))
m=int(input("Multiplos que desea saber:"))

mul=[]

for i in range(1,m+1):
    mul.append(n*i)
print("Los multiplos son:",mul)