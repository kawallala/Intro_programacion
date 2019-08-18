from lista import *
estructura.crear("fraccion","numerador denominador")

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

#menorfrac: fraccion fraccion -> Bool
# determina si la fraccion x es menor que la fraccion y
# ej: menorfrax(fraccion(4,5),fraccion(2,2))-> True
def menorfrac(x,y):
    if comparar(x,y)<0:
        return True
    else:
        return False
assert menorfrac(fraccion(4,5),fraccion(2,2))==True
# test requerido
assert filtro(lista(fraccion(5,4),lista(fraccion(4,8),None)),menorfrac,fraccion(2,1))\
                    ==lista(fraccion(5,4),lista(fraccion(4,8),None))