from cgitb import text


def indexof(texto,buscar,index=0):
    if buscar == "" : return -1

    while index<len(texto):
        if texto[index]==buscar[0]:
            if len(buscar) == 1 : return index
            if index == len(texto)-1: return -1

            indextexto=index+1
            indexbuscar=1
            bbuscar=True
            while bbuscar and indextexto < len(texto) and indexbuscar <len(buscar):
                bbuscar=texto[indextexto]==buscar[indexbuscar]
                indextexto+=1
                indexbuscar+=1
            if bbuscar:return index
        index+=1
    return -1

pal=input("palabra:")
pa=input("palabra a buscar:")

print(indexof(pal,pa))
