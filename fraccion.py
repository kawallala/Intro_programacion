import estructura
from lista import *
#fraccion: numerador (int), denominador (int)
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

assert suma(fraccion(1,2),fraccion(3,4))==fraccion(10,8)




#resta: fraccion fraccion -> fraccion
#resta de fracciones x e y
#ej: resta(fraccion(1,2),fraccion(3,4))->fraccion(-2,8)

def resta(x,y):
  assert esFraccion(x)
  assert esFraccion(y)
  num=x.numerador*y.denominador - \
      x.denominador*y.numerador
  den=x.denominador*y.denominador
  return fraccion(num,den)

assert resta(fraccion(1,2),fraccion(3,4)) \
    == fraccion(-2,8)

#producto: fraccion fraccion -> fraccion
#producto de fracciones x e y
#ej: producto(fraccion(1,2),fraccion(3,4))
#    ->fraccion(3,8)

def producto(x,y):
    assert esFraccion(x)
    assert esFraccion(y)
    num=x.numerador*y.numerador
    den=x.denominador*y.denominador
    return fraccion(num,den)

assert producto(fraccion(1,2),fraccion(3,4)) \
    == fraccion(3,8)

#division: fraccion fraccion -> fraccion
#division fraccion x por fraccion y
#ej: division(fraccion(1,2),fraccion(3,4))
#    ->fraccion(4,6)
def division(x,y):
    assert esFraccion(x)
    assert esFraccion(y)
    num=x.numerador*y.denominador
    den=x.denominador*y.numerador
    f=fraccion(num,den)
    assert esFraccion(f)
    return f
assert division(fraccion(1,2),fraccion(3,4)) \
    ==fraccion(4,6)

#mcd: int int -> int
def mcd(x,y):
  if x>y: return mcd(x-y,y)
  if y>x: return mcd(x,y-x)
  return x

#simplificar: fraccion -> fraccion
#simplifica  una fraccion
#ej: simplificar(fraccion(2,4))->fraccion(1,2)
def simplificar(x):
  assert esFraccion(x)
  m=mcd(x.numerador,x.denominador)
  return fraccion(x.numerador/m, x.denominador/m)
assert simplificar(fraccion(2,4))==fraccion(1,2)



#comparar: fraccion fraccion -> int
#0 si x==y, n>0 si x>y, n<0 si x<y
#ej: comparar(fraccion(1,2),fraccion(2,4))->0
#ej: comparar(fraccion(1,2),fraccion(1,3))->n>0
#ej: comparar(fraccion(1,3),fraccion(1,2))->n<0

def comparar(x,y):
  assert esFraccion(x) and esFraccion(y)
  return x.numerador   * y.denominador - \
         x.denominador * y.numerador

assert comparar(fraccion(1,2),fraccion(2,4))==0
assert comparar(fraccion(1,2),fraccion(1,3))>0
assert comparar(fraccion(1,3),fraccion(1,2))<0

def menorfrac(x,y):
    if comparar(x,y)<0:
        return True
    else:
        return False

def invertir(x):
    esFraccion(x)
    n=fraccion(x.denominador,x.numerador)
    if esFraccion(n): return n
    else:
        return 0

