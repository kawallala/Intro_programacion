import bases
#convertirBases None -> None
#convierte numeros enteros positivos expresados en distintas bases
#ej convertirBases() ->
def convertirBases(suma=0):
    print 'Convertir nº desde base1 a base2'
    base1=input('base? ')   
    if base1==0:
        print 'cantidad de conversiones==',suma
        return
    elif base1<=1 or base1>=11:
        print 'escriba una base valida'
        convertirBases(suma=suma)
    else:
        n=input('nº? ')
        if bases.valido(n,base1)==True:
            base2=input('base2? ')
            if base2<=1 or base2>=11:
                print 'escriba una segunda base valida'
                convertirBases(suma=suma)
            else:
                if base1==base2:
                    print 'nº=',n
                    convertirBases(suma=suma)
                else:
                    a=bases.decimal(n,base1)
                    n2=bases.numero(a,base2)
                    print 'nº=',n2
                    convertirBases(suma=suma+1)
        else:
            print 'escriba un numero escrito correctamente en la base'
            convertirBases(suma=suma)
    
        
