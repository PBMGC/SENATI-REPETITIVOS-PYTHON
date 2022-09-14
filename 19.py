c=int(input("cuantas notas va ingresar:"))
n=[]

if c>=10:
    for i in range(c):
        n.append(int(input("Notas:")))
NM=n[0]
NME=n[0]

M=[]
ME=[]

for x in range(1,len(n)):
    if n[x]>=n[0]:
        M.append(n[x])
    else:
        ME.append(n[x])

PM=0
PME=0

for j in range(len(M)):
    PM+=M[j]
for h in range(len(ME)):
    PME+=ME[h]

print("El promedio mayor:",((PM)//len(M)))
print("El promedio menor es:",((PME)//len(ME)))


