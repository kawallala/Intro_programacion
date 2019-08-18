import mcd
print 'por favor, ingrese numerador y denominador, enteros, de la fraccion'
a=input('numerador? ')
b=input('denominador? ')
if type(a)==int and type(b)==int:
    c=mcd.mcd(a,b)
    print 'la fraccion simplificada es'
    print 'numerador',a/c
    print 'denominador',b/c
else:
    print 'ingrese numeros validos'
