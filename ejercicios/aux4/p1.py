from lista import *

#inv: lista -> lista
#invierte el orden de una lista
#ej: lista(2,lista(3,None))->lista(3,lista(2,None))
def inv(L,l=None):
    assert esLista(L)
    if L==None:
        return l
    else:
        l=lista(cabeza(L),l)
        return inv(cola(L),l)
assert inv(lista(2,lista(3,None)))==lista(3,lista(2,None))
assert inv(None)==None
assert inv(lista(1,None))==lista(1,None)

#pares: lista(int) -> lista(int)
# a partir de una lista L, retorna una lista l con solo los numeros pares
# ej: pares(lista(2,lista(3,None))->lista(2,None)
def pares(L,l=None):
    assert esLista(L)
    if L==None:
        return l
    else:
        if cabeza(L)%2==0:
            l=lista(cabeza(L),l)
            return pares(cola(L),l)
        else:
            return pares(cola(L),l)
assert pares(lista(2,lista(3,None)))==lista(2,None)
assert pares(None)==None
assert pares(lista(1,lista(3,None)))==None
assert filtro(lista(2,lista(3,None)),lambda x,y:x%y==0,2)==lista(2,None)
assert filtro(lista(1,lista(3,None)),lambda x,y:x%y==0,2)==None
assert filtro(None,lambda x,y:x%y==0,2)==None

# menor: lista(int) -> num
# retorna el manor valor x de una lista L
#
def menor(L,x=0,n=0):
    assert esLista(L)
    if n==0:
        if L==None:
            return 'error'
        x=cabeza(L)
        return menor(cola(L),x,1)
    else:
        if L == None: return x
        if cabeza(L)<x:
            x=cabeza(L)
            return menor(cola(L),x,n)
        else:
            return menor(cola(L),x,n)
assert menor(lista(1,None))==1
assert reductor(lista(1,None),lambda x,y:x<y,99999999)==1
