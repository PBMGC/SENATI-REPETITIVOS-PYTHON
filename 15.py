def convertidor(x):
    texto=x
    Mayusculas=["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "Ñ" , "O" , "P" , "Q" , "R" , "S" ,"T" , "U" , "V" , "W" , "X" , "Y" , "Z" ]
    minusculas=["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "ñ" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
    rptaM=""
    rptami=""
    for i in texto:
        if i in Mayusculas: i=minusculas[(Mayusculas.index(i))]
        rptami+=i
        if i in minusculas: i=Mayusculas[(minusculas.index(i))]
        rptaM+=i

    if rptaM!=texto:
        print("MAYUSCULAS:",rptaM)
    else:
        print("minusculas:",rptami)

    


n=input("Palabra a convertir:")
convertidor(n)
