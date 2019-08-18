from AB import *
from lista import *
A=AB(2, AB(5,AB(7,None,None),AB(8,None,None)), AB(3,AB(6,None,None),None))

#esHeap: AB -> bool
#True si A es un heap
#menor arriba y heaps a la izquierda y derecha
#ej: esHeap(A)->True
def esHeap(A):
    assert esAB(A)
    if A==None: return True
    v=A.valor
    p=A.izq==None or v<=A.izq.valor and esHeap(A.izq)
    q=A.der==None or v<=A.der.valor and esHeap(A.der)
    return p and q
assert esHeap(A)

#agregar: any AB -> AB
#agregar x a A 
#ej: agregar(1,AB(2,None,None))->AB(1,AB(2,None,None),None)
def agregar(x,A):
    assert esAB(A)
    if A==None: return AB(x,None,None)
    m=min(x,A.valor); M=max(x,A.valor)
    if altura(A.izq) <= altura(A.der):
        return AB(m, agregar(M,A.izq), A.der)
    else:
        return AB(m, A.izq, agregar(M,A.der))
assert agregar(1,AB(2,None,None))==AB(1,AB(2,None,None),None)


#borrarMenor: AB -> AB
#borrar (eliminar) primer valor de A
#ej: borrarMenor(AB(1,AB(2,None,None),AB(3,None,None)))->AB(2,None,AB(3,None,None))
def borrarMenor(A):
    assert esAB(A)
    if A==None: return None
    if A.izq==None: return A.der
    if A.der==None: return A.izq
    v1=A.izq.valor; v2=A.der.valor
    if v1<=v2:
        return AB(v1,borrarMenor(A.izq),A.der)
    else:
        return AB(v2,A.izq,borrarMenor(A.der))
assert borrarMenor(AB(1,AB(2,None,None),AB(3,None,None)))==AB(2,None,AB(3,None,None))

L=lista(2,lista(3,lista(1,None)))

#aHeap: lista -> AB
#AB (heap) con valores de lista L
#ej: heap(L)->AB(1,AB(2,None,None),AB(3,None,None))
def aHeap(L):
    assert esLista(L)
    if L==None: return None
    return agregar(cabeza(L),aHeap(cola(L)))
assert aHeap(L)==AB(1,AB(3,None,None),AB(2,None,None))

#aLista: AB -> lista
#lista con elementos ordenados de A
#ej:aLista(AB(1,AB(2,None,None),None))->lista(1,lista(2,None))
def aLista(A):
    assert esAB(A)
    if A==None: return None
    return lista(A.valor,aLista(borrarMenor(A)))
assert aLista(AB(1,AB(2,None,None),None))==lista(1,lista(2,None))
    
#heapSort: lista -> lista
#L ordenada
#ej: heapsort(L)->lista(1,lista(2,lista(3,None)))
def heapsort(L):
    assert esLista(L)
    return aLista(aHeap(L))
assert heapsort(L)==lista(1,lista(2,lista(3,None)))
    
        
