from conjunto import *

#leer: int -> lista
#coloca los numeros ingresados en una lista que representa al conjunto n, retornando esta ultima
#ej: leer(A) -> lista(1,lista(2,lista(3,None)))
def leer(n,c=None,fin='.'):    
    e=raw_input('elemento?')
    if e==fin:
        print n+'='+str(c)
        print 'Cardinal='+a_str(cardinal(c))        
        return c
    else:
        c=lista(e,c)
        return leer(n,c,fin)

#operacion: lista lista ->lista
#toma dos lista y opera segun la operacion ingresada
#ej: operacion(lista(1,lista(2,None)),lista(3,None))
def operacion(A,B,fin='.'):
    assert esConjunto(A) and esConjunto(B)
    print ' '
    op=raw_input('Operacion(+*-=<>.)?')
    if op==fin:
        return
    if op=='+' or op=='*' or op=='-':
        if op=='+':            
            y=union(A,B)            
            print 'A union B=',
        if op=='*':
            y=inter(A,B)
            print 'A intreseccion B',
        if op=='-':
            y=resta(A,B)
            print 'A-B',
        print str(y)
        print 'Cardinal='+a_str(cardinal(y))
        operacion(A,B,fin)
    else:
        if op=='=':
            y=igual(A,B)
            print 'A=B es',
        if op=='<':
            y=sub(A,B)
            print 'A<B es',
        if op=='>':
            y=super(A,B)
            print 'A>B es',
        if y:
            print 'Si'
        else:
            print 'No'
        operacion(A,B,fin)


def Prueba():
    print'ingrese elementos Conjunto A (o . para terminar)'
    A=leer('A')
    print ' '
    print 'ingrese elementos Conjunto B (o . para terminar)'
    B=leer('B')
    operacion(A,B)
    x=raw_input('Otros conjuntos(si/no)?')
    if x=='si':
        Prueba()
    if x=='no':
        return
Prueba()
                 
                
        
