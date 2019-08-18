import bases
def func(i=0,b=0):
        n=input('n°? ')
        if n==0:
                a=bases.numero(i,b)
                print 'menor: base=',b,'digitos=',a,'decimal=',i
        elif n/10==0:
                print 'escriba la base y el numero'
                func(i,b)
        else:
                base=bases.primero(n)
                if base<=1 or base>10:
                        print 'base incorrecta'
                        func(i,b)
                else:
                        numero=bases.ultimos(n)
                        if bases.valido(numero,base):
                                d=bases.decimal(numero,base)
                                print 'decimal=',d
                                if i==0:
                                        i=d
                                        b=base
                                        func(i,b)
                                elif d<i:
                                        i=d
                                        b=base
                                        func(i,b)
                                else:
                                        func(i,b)
                        else:
                                print 'numero incorrecto'
                                func(i,b)

