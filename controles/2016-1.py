from lista import *
estructura.crear("fecha","dia mes año")
estructura.crear("personaje","nombre nace muere")
p1=personaje("b",fecha(17,1,1876),fecha(28,4,1934))
p2=personaje("c",fecha(7,5,1853),fecha(11,9,1935))
p3=personaje("a",fecha(28,4,1921),fecha(20,1,2000))

#hoy lista(personaje) fecha -> lista(personajes)
#determina que personas murieron o nacieron en una fecha dada

def hoy(L,f):
    assert esLista(L)
    assert type(f)==fecha
    if L==None:
        return None
    if L.cabeza.nace.dia==f.dia and L.cabeza.nace.mes==f.mes:
        return lista(L.cabeza)
estructura.crear("AB", "valor izq der")