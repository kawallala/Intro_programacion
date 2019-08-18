agenda=[["a",2],["c",1],["d",4]]
#buscar: str list(list) -> int
#buscar el fono de una persona en base a la agenda hecha de listas
#ej: buscar("a",agenda) -> 2
#ej: buscar("b",agenda) -> None
def buscar(nombre, L):
    assert type(L)==list
    for i in L:
        if i[0]==nombre:
            return i[1]
    return

assert buscar("a",agenda)
assert not buscar("b",agenda)