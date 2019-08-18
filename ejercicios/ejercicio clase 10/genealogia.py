from lista import *
#persona: nombre(str) nacimiento(int) padre(persona) madre(persona) hijos(lista(personas))
estructura.crear("persona", "nombre nacimiento padre madre hijos")


#primera generacion ("abuelos")
carlos=persona("carlos",1926,None,None,None)
beatriz=persona("beatriz",1926,None,None,None)

#segunda generacion ("hijos")
andres=persona("andres",1950,carlos,beatriz,None)
david=persona("david",1955,carlos,beatriz,None)
eva=persona("eva",1965,carlos,beatriz,None)
federico=persona("federico",1966,None,None,None)

#tercera generacion ("nietos")
gustavo=persona("gustavo",1996,federico,beatriz,None)

#completando con datos de padres, madres e hijos
eva.hijos=lista(gustavo,None)
federico.hijos=lista(gustavo,None)
carlos.hijos=lista(andres,lista(david,lista(eva,None)))
beatriz.hijos=lista(andres,lista(david,lista(eva,None)))


#esPadeDe: persona persona -> bool
#True si x es padre o madre de y
#ej esPadreDe(carlos,eva) -> True
#ej esPadreDe(beatriz,federico) -> False
def esPadreDe(x,y):
    assert type(x)==persona and type(y)==persona
    return x==y.padre or x==y.madre
assert esPadreDe(carlos,eva)
assert not esPadreDe(beatriz,federico)

#esAncestro: persona persona -> bool
#True si x es ancestro de P
#ej: esAncestro(carlos,gustavo) -> True
#ej: esAncestro(beatriz,federico) -> False
def esAncestro(x,P):
    assert type(x)==persona and type(P)==persona
    p=P.padre!=None and P.padre==x or esAncestro(x,P.padre)
    q=P.madre!=None and P.madre==x or esAncestro(x,P.madre)
    return q or p
assert esAncestro(carlos,gustavo)
assert not esAncestro(beatriz,federico)

#ancestro: persona -> lista(persona)
#ancestros de P
#ej: ancestros(david)->lista(carlos,lista(beatriz,None))
def ancestros(P):
    assert P==None or Type(P)==persona
    if P==None: return None
    if P.padre==None:
        L1=None
    else:
        L1=lista(P.padre,ancestros(P.padre))
    if P.madre==None:
        L2=None
    else:
        L2=lista(P.madre,ancestros(P.madre))
    return juntar(L1,L2)
assert ancestros(david)==lista(carlos,lista(beatriz,None))

#juntar: lista lista -> lista
#lista con L1 y a continuacion L2
#ej: juntar(lista(1,lista(2,None)),lista(3,lista(4,None))) -> lista(1,lista(2,lista(3,lista(4,None))))
def juntar(L1,L2):
    assert esLista(L1) and esLista(L2)
    if L1==None: return L2
    return lista(cabeza(L1),juntar(cola(L1),L2))
assert juntar(lista(1,lista(2,None)),lista(3,lista(4,None)))==lista(1,lista(2,lista(3,Lista(4,None))))

