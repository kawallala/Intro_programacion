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