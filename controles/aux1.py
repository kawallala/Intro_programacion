from lista import *
#sumaproductos: lista(int) lista(int) -> int
#considera a partir de dos listas retorna un entero como la suma
#ej: sumaproductos(lista(1,lista(2,None)),lista(3,lista(4,None))) -> 1*3+2*4
def sumaproductos(A,B,i=0):
    assert type(A)==lista and type(B)==lista
    n=cabeza(A)*cabeza(B)
    l=i+n
    if cola(A)==None or cola(B)==None:
        return l
    return sumaproductos(cola(A),cola(B),l)
print sumaproductos(lista(1,lista(2,None)),lista(3,None))
#alumno: run(str) puntajes(lista(int))
estructura.crear("alumno", "run puntajes")
def seleccionar(L,puntajeMinimo):
    assert esLista(L)
    if L==None:
        return
    p=cabeza(L)
    m=lista(10,lista(20,lista(10,lista(45,lista(15,None)))))
    if sumaproductos(p.puntajes,m)>puntajeMinimo:
        return lista(p.run,lista(seleccionar(cola(L),puntajeMinimo)))
    return seleccionar(cola(L),puntajeMinimo)

def filtrar(arbol,X,Y,arbolfinal =None)
    if arbol==None:
        return None
        if arbol.valor<x
            return filtrar(arbol.der)