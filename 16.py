def rever(x):
    
    palabra=x
    palabrarev= ""

    for i in palabra:
        palabrarev= i + palabrarev
    
    print("Palabra al revez:",palabrarev)

pa=input("Palabra:")
rever(pa)

