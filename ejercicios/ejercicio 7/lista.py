# coding=utf-8
import estructura
# lista: valor(any) siguiente(lista)
estructura.crear("lista","valor siguiente")

# esLista: lista -> bool
# determina si un elemento es del tipo lista
# ej: esLista(None)-> True
# ej: esLista(lista("a",None))->True
# ej: esLista(2)->True
def esLista(L):
    return L==None or type(L)==lista
assert esLista(None)==True
assert esLista(lista("a",None))==True
assert not esLista(2)

# cabeza: lista -> any
# primer valor de una lista
# ej: cabeza(lista('a',lista("b",None))) -> "a"

def cabeza(L):
    assert esLista(L)
    return L.valor
assert cabeza(lista("a",lista("b", None)))=="a"

# cola: lista -> lista
# devuelve lista sin el primer valor
#ej: cola(lista("a",lista("b",None)))->lista("b",None)
#ej: cola(lista("a",None))->None

def cola(L):
    assert esLista(L)
    return L.siguiente
assert cola(lista("a",lista("b",None)))==lista("b",None)
assert cola(lista("a",None))==None

# enLista: int lista -> bool
# determina si un número está presente en una lista
# ej: enLista(3,lista(3,lista(2,None))) -> True
# ej: enLista(2,None) -> False
def enLista(x,L):
    assert esLista(L)
    if L==None:
        return False
    elif cabeza(L)==x:
        return True
    else:
        return enLista(x,cola(L))
assert enLista(3,lista(3,lista(2,None)))==True
assert not enLista(2,None)