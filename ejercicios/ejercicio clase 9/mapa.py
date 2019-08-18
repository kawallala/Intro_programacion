
from lista import *
estructura.crear("fraccion","numerador denominador")

#mapa: (any->any) lista(any) -> lista(any)
#lista aplicando funcion a valores de L
#ej: mapa(f,lista(5,lista(4,None))) -> lista(f(5),lista(f(4),None))

def mapa(funcion,L):
  assert esLista(L)
  if L==None:
    return None
  else:
    return lista(funcion(cabeza(L)),mapa(funcion,cola(L)))
assert mapa(lambda x: 5 * x, lista(5, lista(4, None))) == lista(25, lista(20, None))
#esFraccion: fraccion->bool
#True si es una fraccion valida
#ej: esFraccion(fraccion(1,2))->True
#ej: esFraccion(fraccion(1,0))->False
def esFraccion(x):
    return type(x)==fraccion \
       and type(x.numerador)==int \
       and type(x.denominador)==int \
       and x.denominador!=0
assert esFraccion(fraccion(1,2))
assert not esFraccion(fraccion(1,0))


# invertir fraccion-> fraccion
# invierte el numerador y denominador de una fraccion
#ej: invertir(fraccion(2,1))-> fraccion(1,2)
#ej: invertir(fraccion(0,1))-> fraccion(0,1)
def invertir(x):
    esFraccion(x)
    n=fraccion(x.denominador,x.numerador)
    if esFraccion(n): return n
    else:
        return fraccion(0,1)
assert invertir(fraccion(2,1))==fraccion(1,2)
assert invertir(fraccion(0,1))==fraccion(0,1)



assert mapa(invertir,lista(fraccion(5,4),lista(fraccion(4,8),None)))==lista(fraccion(4,5),lista(fraccion(8,4),None))