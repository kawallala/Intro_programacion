from lista import *
a_str=str

# esConjunto: lista(num) -> bool
# determina si una lista L es conjunto
# ej: esConjunto(lista(2,lista(3,None))-> True
# ej: esConjunto(lista(2,lista(2,None))->False
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
# ej: pertenece(5,lista(2,lista(3,None)))-> False
def pertenece(n, L):
    assert esConjunto(L)
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
#intersecta 2 conjuntos representados por listas
#ej:inter(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None))) -> lista(None)
#ej:inter(lista(5,lista(4,None)), lista(4,None)) -> lista(4,None)

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


#union: lista(num) lista(num) -> lista(num)
#une 2 conjuntos representados por listas
#ej:union(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))
# -> lista(3,lista(1,lista(2,lista(5,lista(4,None)))))
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
assert union(lista(5,lista(4,None)),lista(4,None))==lista(5,lista(4,None))
assert union(None,lista(4,lista(2,None)))==lista(4,lista(2,None))
assert union(lista(4,lista(2,None)),None)==lista(2,lista(4,None))


#resta: lista(num) lista(num) -> lista(num)
#devuelve un conjunto con todos los elementos de s que no estan en y
#ej: resta(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))-> lista(3,lista(1,lista(2,None)))
#ej: resta(lista(3,lista(1,lista(2,None))), lista(3,lista(2,None)))-> lista(1,None)

def resta(x,y,l=None):
    assert esConjunto(x)
    assert esConjunto(y)
    if x==None: return l
    if pertenece(cabeza(x),y):
        return resta(cola(x),y,l)
    else:
        l=lista(cabeza(x),l)
        return resta(cola(x),y,l)
assert resta(lista(3,lista(1,lista(2,None))),lista(5,lista(4,None)))==lista(2,lista(1,lista(3,None)))
assert resta(lista(3,lista(1,lista(2,None))), lista(3,lista(2,None)))==lista(1,None)


#igual: lista(num) lista(num)-> bool
#devuelve True si 2 conjuntos son iguales
#ej:igual(lista(3,lista(1,lista(2,None))), lista(3,lista(2,None)))->False
#ej:igual(lista(6,lista(5,lista(3,None))), lista(3,lista(5,lista(6,None))))->True
def igual(x,y,n=0):
    assert esConjunto(x)
    assert esConjunto(y)
    if n==0:
        if cardinal(x)==cardinal(y):
             if x==None: return True
             if pertenece(cabeza(x),y):
                 return igual(cola(x),y,n=n+1)
             else:
                 return False
        else:
            return False
    else:
        if x==None: return True
        if pertenece(cabeza(x),y):
            return igual(cola(x),y,n)
        else:
            return False
assert igual(lista(3,lista(1,lista(2,None))), lista(3,lista(2,None)))==False
assert igual(lista(6,lista(5,lista(3,None))), lista(3,lista(5,lista(6,None))))==True


#sub: lista(num) lista(num)-> bool
#True si el conjunto x es subconjunto de y
#ej:sub(lista(2,lista(3,None)),lista(6,lista(2,lista(3,None))))->True
#ej:sub(lista(7,lista(3,None)),lista(6,lista(2,lista(3,None))))->False
#ej:sub(None,lista(7,lista(3,None)))->True

def sub(x,y):
    assert esConjunto(x) and esConjunto(y)
    if igual(x,y): return True
    if cardinal(x)<cardinal(y):
        if x==None: return True
        if pertenece(cabeza(x),y):
            return sub(cola(x),y)
        else:
            return False
    else:
        return False
assert sub(lista(2,lista(3,None)),lista(6,lista(2,lista(3,None))))==True
assert sub(lista(7,lista(3,None)),lista(6,lista(2,lista(3,None))))==False
assert sub(None,lista(7,lista(3,None)))==True


#super: lista(num) lista(num)-> bool
#True si el conjunto y es subconjunto de x
#ej:super(lista(2,lista(3,None)),lista(6,lista(2,lista(3,None))))->False
#ej:super(lista(7,lista(3,None)),lista(3,None))->True
#ej:super(lista(8,lista(5,None)),None)->True
def super(x,y):
    assert esConjunto(x) and esConjunto(y)
    if cardinal(x)<cardinal(y):
        return False
    else:
        return sub(y,x)
assert super(lista(2,lista(3,None)),lista(6,lista(2,lista(3,None))))==False
assert super(lista(7,lista(3,None)),lista(3,None))==True
assert super(lista(8,lista(5,None)),None)==True


#str: lista(num)-> str
#devuelve el conjunto como un string
#ej:str(lista(6,lista(2,lista(3,None))))->'{6,2,3}
#ej:str(None)->'{}'
def str(x,s='{'):
    assert esConjunto(x)
    if x==None:  return s+'}'
    if cardinal(x)==1:
        s=s+a_str(cabeza(x))
        return str(cola(x),s)
    else:
        s=s+a_str(cabeza(x))+','
        return str(cola(x),s)

assert str(None)=='{}'
assert str(lista(2,lista(4,None)))=='{2,4}'


