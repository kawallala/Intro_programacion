# valido: num num -> bool
# determina si un numero entero no negativo esta escrito en la base correcta entre 2 y 10
# ej: valido(102,3) -> True
# ej: valido(102,2) -> False
def valido(a, b):
    assert type(a) == int and a >= 0
    assert type(b) == int and b >= 2 and b <= 10
    if (a % 10) < b:
        if a / 10 == 0:
            return True
        else:
            return valido(a / 10, b)
    else:
        return False
