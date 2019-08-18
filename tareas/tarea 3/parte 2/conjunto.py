a_str=str
#esConjunto: list(num) -> bool
#determina si una lista L es conjunto
#ej: esConjunto(L=[1,2,3])-> True
#ej: esConjunto(L=[2,2]) -> False
#ej: esConjunto(L=[]) -> True
def esConjunto(L):
    assert type(L)==list
    if L==[]: return True
    M=[]
    for i in L:
        assert type(i)==int or type(i)==float
        if i in M:
            return False
        if i not in M:
            M.append(i)
    return True
assert esConjunto(L=[1,2,3])
assert not esConjunto(L=[2,2])
assert esConjunto(L=[])

#union: list(num) list(num) -> list(num)
#une 2 conjuntos representados por listas
#ej: union([1,2,3],[4,5,6] -> [1,2,3,4,5,6]
#ej: union([1,2],[2]) -> [1,2]
#rj: union([],[1]) -> [1]
def union(L1,L2):
    assert esConjunto(L1)
    assert esConjunto(L2)
    for i in L2:
        if i not in L1:
            L1.append(i)
    return L1
assert union([1,2,3],[4,5,6])==[1,2,3,4,5,6]
assert union([1,2],[2]) == [1,2]
assert union([],[1]) == [1]

#inter: list(num) list(num) -> list(num)
#intersecta 2 conjuntos representados por listas
#ej: inter([3,2,1],[4,5] -> []
#ej: inter([5,4],[4]) ->[4]
def inter(L1,L2):
    assert esConjunto(L1)
    assert esConjunto(L2)
    M=[]
    for i in L1:
        if i in L2:
            M.append(i)
    return M
assert inter([3,2,1],[4,5])==[]
assert inter([5,4],[4])

#pertenece: int list(num) -> bool
# determina si un numero n pertenece a una lista L
#ej: pertenece(1,[1,2,3]) -> True
# ej: pertence(1,[3,4]) -> False
def pertenece(n,L):
    assert esConjunto(L)
    return n in L
assert pertenece(1,[1,2,3])
assert not pertenece(1,[3,4])

#cardinal: list(num) -> bool
#calcula el cardinal de un conjunto representado por una lista
#ej: cardinal([]) -> 0
#ej: cardinal([1,2,3]) -> 3
def cardinal(L,n=0):
    assert esConjunto(L)
    for i in L:
        n+=1
    return n
assert cardinal([])==0
assert cardinal([1,2,3])==3

#resta: list(num) list(num) -> list(num)
#devuelve una lista con los elementos de L1 que no estan en L2
#ej: resta([1,2,3],[4,5]) -> [1,2,3]
#ej: resta([1,2,3],[1,2]) -> [3]
#ej: resta([1,2],[1,2]) -> []
def resta(L1,L2):
    assert esConjunto(L1)
    assert esConjunto(L2)
    for i in L2:
        if i in L1:
            L1.remove(i)
    return L1
assert resta([1,2,3],[4,5])==[1,2,3]
assert resta([1,2,3],[1,2])==[3]
assert resta([1,2],[1,2])==[]

#igual: list(num) list(num) -> list(num)
#retorna True si 2 onjuntos contienen a los mismos elementos
#ej: igual([1,2],[2,1]) -> True
#ej: igual([1,2],[3,4]) -> False
def igual(L1,L2):
    assert esConjunto(L1) and esConjunto(L2)
    for i in L1:
        if i not in L2:
            return False
    return True
assert igual([1,2],[2,1])
assert not igual([1,2],[3,4])

#sub: list(num) list(num) -> bool
#True si L1 es subconjunto de L2
#ej: sub([2,3],[6,5,4,3,2]) -> True
#ej: sub([1,2], [3,4]) -> False
def sub(L1,L2):
    assert esConjunto(L1) and esConjunto(L2)
    if igual(L1,L2): return True
    if cardinal(L1)>cardinal(L2): return False
    for i in L1:
        if i not in L2:
            return False
    return True
assert sub([2,3],[6,5,4,3,2])
assert not sub([1,2],[3,4])

#super: list(num) list(num) -> bool
# retorna True si L1 es superconjunto de L2
#ej: super([6,5,4,3,2,1],[3,2]) -> True
#ej: super([1,2],[3,4]) -> False
def super(L1,L2):
    assert esConjunto(L1) and esConjunto(L2)
    if cardinal(L1)<cardinal(L2): return False
    return sub(L2,L1)
assert super([6,5,4,3,2,1],[3,2])
assert not super([1,2],[3,4])

#str: list(num) -> str
#devuelve un string representando al conjunto:
#ej:str([1,2,3]) -> '{1,2,3}'
#ej: str([]) -> '{}'
def str(L,s='{'):
    assert esConjunto(L)
    if L==[]: return '{}'
    for i in range(len(L)-1):
        s=s+a_str(L[i])+','
    s=s+a_str(L[len(L)-1])
    return s+'}'
assert str([])=='{}'
assert str([1,2,3])=='{1,2,3}'