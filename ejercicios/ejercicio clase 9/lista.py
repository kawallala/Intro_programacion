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

#filtro: lista(any) (any any->bool) any -> lista(any)
#lista con valores de L que cumplen comparacion con x
#ej:filtro(lista(5,lista(4,None)),menorQue,5)->lista(4,None)

def filtro(L,comparacion,x):
  assert esLista(L)
  if L==None: return None

  if comparacion(cabeza(L),x):
    return lista(cabeza(L),filtro(cola(L),comparacion,x))
  else:
    return filtro(cola(L),comparacion,x)
assert filtro(lista(9,lista(4,None)),lambda x,y: x>y,6)==lista(9,None)

#mapa: (any->any) lista(any) -> lista(any)
#lista aplicando funcion a valores de L
#ej: mapa(f,lista(5,lista(4,None))) -> lista(f(5),lista(f(4),None))

def mapa(funcion,L):
  assert esLista(L)
  if L==None:
    return None
  else:
    return lista(funcion(cabeza(L)),mapa(funcion,cola(L)))

assert mapa(lambda x:5*x,lista(5,lista(4,None)))==lista(25,lista(20,None))

#reductor: lista (any any->any) any -> any
#operación con todos los valores de L
#acumulando en resultado

def reductor(L,operacion,resultado):
  assert type(L)==lista
  r=operacion(resultado,cabeza(L))
  if cola(L)==None:
    return r
  else:
    return reductor(cola(L),operacion,r)

assert reductor(lista(5,lista(5,None)),lambda x,y:x+y,0)