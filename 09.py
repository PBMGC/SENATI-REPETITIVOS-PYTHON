altura=int(input("altura del rectangulo:"))
print()
for i in range(1,altura+1):
    if i==1 or i==altura:
        for j in range(2*altura):
            print("* ",end="")
    else:
        for h in range(1,2*altura+1):
            if h==1 or h==2*altura:
                print("* ",end="")
            else:
                print("  ",end="")
    print()
print()