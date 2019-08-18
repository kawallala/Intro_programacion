
from lista import *
estructura.crear("fraccion","numerador denominador")


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


#suma: fraccion fraccion -> fraccion
#suma de fracciones x e y
#ej: suma(fraccion(1,2),fraccion(3,4))->fraccion(10,8)

def suma(x,y):
  assert esFraccion(x)
  assert esFraccion(y)
  num = x.numerador * y.denominador + \
        x.denominador * y.numerador
  den = x.denominador * y.denominador
  return fraccion(num,den)

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
assert reductor(lista(fraccion(4,5),lista(fraccion(3,8),None)),suma,fraccion(0,1))==fraccion(47,40)