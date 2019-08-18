from lista import *

#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB","valor izq der")

#juntar: lista lista -> lista
#lista con L1 y a continuacion L2
#ej: juntar(lista(1,lista(2,None)),lista(3,lista(4,None))) -> lista(1,lista(2,lista(3,lista(4,None))))
def juntar(L1,L2):
    assert esLista(L1) and esLista(L2)
    if L1==None: return L2
    return lista(cabeza(L1),juntar(cola(L1),L2))
assert juntar(lista(1,lista(2,None)),lista(3,lista(4,None)))==lista(1,lista(2,lista(3,lista(4,None))))

A=AB(5,AB(6,AB(3,None,None),AB(2,None,None)),AB(2,AB(4,None,None),None))

#esAB: any -> bool
#True si x es un AB
#ej: esAB(A)->True
#ej: esAB(None)->True

def esAB(x):
    return x==None or type(x)==AB
assert esAB(A)
assert esAB(None)


#valores: AB -> int
#cantidad de valores de A
#ej: valores(A)->6
#ej: valores(None)->0

def valores(A):
    assert esAB(A)
    if A==None:
        return 0
    else:
        return 1+valores(A.izq)+valores(A.der)
assert valores(A)==6
assert valores(None)==0


#hojas: AB->int
#cantidad de hojas de A
#ej: hojas(A)->3
#ej:hojas(None)->0

def hojas(A):
    assert esAB(A)
    if A==None:
        return 0
    elif A.der==None and A.izq==None:
        return 1
    else:
        return hojas(A.izq)+hojas(A.der)
assert hojas(A)==3
assert hojas(None)==0


#altura: AB -> int
#n de niveles de A
#ej: altura(A)->3
#ej:altura(AB(1,None,AB(2,None,None))->2

def altura(A):
    assert esAB(A)
    if A==None:return 0
    return 1+max(altura(A.izq),altura(A.der))
assert altura(A)==3
assert altura(AB(1,None,AB(2,None,None)))==2
assert altura(None)==0

#################################################################
A=AB("-",AB(2,None,None),AB("*",AB(3,None,None),AB(4,None,None)))

#evaluar: AB-> num
#resultado de la expresion representada en A
#ej: evaluar(A)->-10
def evaluar(A):
    assert type(A)==AB
    if A.izq==None and A.der==None: return A.valor
    a=evaluar(A.izq)
    b=evaluar(A.der)
    op=A.valor
    if op=="+": return a+b
    if op=="-": return a-b
    if op=="*": return a*b
    if op=="/":
        assert b!=0
        return a/b
assert evaluar(A)==-10

#################################################################
A=AB(4,AB(2,AB(1,None,None),AB(3,None,None)),AB(6,AB(5,None,None),None))

#enABB: any AB -> bool
#True si x esta en A
#ej: enABB(3,A)->True
#ej: enABB(7,A)->False

def enABB(x,A):
    assert esAB(A)
    if A==None: return False
    if x<A.valor: return enABB(x,A.izq)
    if x>A.valor: return enABB(x,A.der)
    return True
assert enABB(3,A)
assert not enABB(7,A)


#insertar: any AB -> AB
#nuevo ABB igual que A pero con x
#ej: insertar("A",AB("B",None,None)) -> AB("B",AB("A",None,None),None)
#ej: insertar("C",AB("B",None,None)) -> AB("B",None,AB("C",None,None))
#ej: insertar("B",None) -> AB("B",None,None)

def insertar(x,A):
    assert esAB(A)
    if A==None: return AB(x,None,None)
    v=A.valor
    if x<v:
        return AB(v,insertar(x,A.izq),A.der)
    if x>v:
        return AB(v,A.izq,insertar(x,A.der))
    return A
assert insertar("A",AB("B",None,None))==AB("B",AB("A",None,None),None)
assert insertar("C",AB("B",None,None))==AB("B",None,AB("C",None,None))
assert insertar("B",None)==AB("B",None,None)


#escribir: AB -> None
#escribir valores de ABB A en orden ascendente
#ej: escribir(A) -> 1,2,3,4,5,6
def escribir(A):
    assert esAB(A)
    if A==None: return
    escribir(A.izq)
    print A.valor
    escribir(A.der)


#aLista: AB-> lista
#convertir A a lista(ordenada por valores)
# aLista(A) -> lista(1,lista(2,lista(3,lista(4,lista(5,lista(6,None))))))

def aLista(A):
    assert esAB(A)
    if A==None: return
    a=aLista(A.izq)
    c=lista(A.valor,None)
    b=aLista(A.der)
    return juntar(a,juntar(c,b))

assert aLista(A)==lista(1,lista(2,lista(3,lista(4,lista(5,lista(6,None))))))

#ordenar: lista -> lista
#entregar lista ordenada en arden ascendente

def ordenar(L):
    assert esLista(L)
    if L==None: return
    B=insertar(cabeza(L),None)
    ordenar(cola(L))
    return B
print ordenar(lista(3,lista(2,lista(1,None))))