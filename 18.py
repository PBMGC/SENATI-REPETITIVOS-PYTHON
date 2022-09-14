def ltrim(texto):
    x=0
    while x<len(texto) and texto[x]== " " : x+=1
    return texto[x:]

def rtrim(texto):
    x=len(texto)-1
    while x>0 and texto[x]== " " : x-=1
    return texto[:x+1]

def trim(texto):
    return rtrim(ltrim(texto))

palabra=input("palabra:")
fun=input("funcion a aplicar:")
if fun=="ltrim":
    print(ltrim(palabra))
elif fun=="rtrim":
    print(rtrim(palabra))
else:
    print(trim(palabra))   
 
    
