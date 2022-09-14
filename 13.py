multiplos3=[]
for i in range(1,101):
    if i%3==0:
        if i%5!=0:
            multiplos3.append(i)
print("Numeros multiplos de 3 pero no de 5:")
print(multiplos3)

s=0
for x in range(len(multiplos3)):
    s+=multiplos3[x]
print("la suma total es:",s)