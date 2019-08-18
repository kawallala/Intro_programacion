from lista import *

# esConjunto: lista(num) -> bool
# determina si una lista L es conjunto
# ej: esConjunto(lista(2,lista(3,None))-> True
# ej: esConjunto(lista(2,lista(2,None))->True
# ej: esConjunto(None)->True
def esConjunto(L):
    assert esLista(L)
    if L == None: return True
    if enLista(cabeza(L), cola(L)):
        return False
    else:
        return esConjunto(cola(L))
assert not esConjunto(lista(3, lista(3, None)))
assert esConjunto(lista(2, lista(3, None))) == True
assert esConjunto(None) == True


# pertenece: int lista(num) -> bool
# determina si un elemento l esta en una lista L
# ej: pertenece(2,lista(2,lista(3,None)))-> True
# ej: pertenece(5,lista(2,lista(3,None)))-> True
def pertenece(n, L):
    assert type(n) == int
    assert esLista(L)
    return enLista(n, L)
assert pertenece(2, lista(2, lista(3, None))) == True
assert pertenece(5, lista(2, lista(3, None))) == False

#cardinal: lista(num) -> int
# determina el cardinal de un conjunto
# ej: cardinal(None)->0
# ej: cardinal(lista(2,lista(3,lista(4,None))))->3

def cardinal(L,n=0):
    assert esConjunto(L)
    if L==None:
        return n
    else:
        return cardinal(cola(L),n=n+1)
assert cardinal(None)==0
assert cardinal(lista(2,lista(3,lista(4,None))))==3

#inter: lista(num) lista(num) -> lista(num)
#intersecciona 2 conjuntos representados por listas
#ej:inter(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None))) -> None
#ej:inter(lista(5,lista(4,None)), lista(4,None)) -> lista(4,None)
#ej:inter(None,lista(2,lista(3,None)))->None

def inter(x,y,l=None):
    assert esConjunto(x)
    assert esConjunto(y)
    if x==None: return l
    if pertenece(cabeza(x),y):
       l=lista(cabeza(x),l)
       return inter(cola(x),y,l)
    else:
        return inter(cola(x),y,l)
assert inter(lista(5,lista(4,None)), lista(4,None))==lista(4,None)
assert inter(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))== None
assert inter(None,lista(2,lista(3,None)))== None

#union: lista(num) lista(num) -> lista(num)
#une 2 conjuntos representados por listas
#ej:union(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))
# -> lista(2,lista(1,lista(3,lista(5,lista(4,None)))))
#ej:union(lista(5,lista(4,None)), lista(4,None)) -> lista(5,lista(4,None))
#ej:union(None,lista(4,lista(2,None)))-> lista(4,lista(2,None))

def union(x,y):
    assert esConjunto(x)
    assert esConjunto(y)
    if x==None: return y
    if pertenece(cabeza(x),y):
        return union(cola(x),y)
    else:
        y=lista(cabeza(x),y)
        return union(cola(x),y)
assert union(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))==lista(2,lista(1,lista(3,lista(5,lista(4,None)))))
assert union(None,lista(4,lista(2,None)))==lista(4,lista(2,None))
assert union(lista(4,lista(2,None)),None)==lista(2,lista(4,None))

