#valor: int, str -> int
#determina el valor de un dato a partir de un numero n, que contiene los datos
#en los digitos correspondientes
#ej: valor(203503200, edad) -> 35
def valor(n,s):
    assert type(n)==int and type(s)==str
    if s=='sexo':
        return n/100000000
    elif s=='edad':
        return n/100000%1000
    elif s=='hijos':
        return n/1000%100
    elif s=='estado civil':
        return n/100%10
    elif s=='pais':
        return n%100
    else:
        return -1
assert valor(203503200,'edad')==35
assert valor(203503200,'sexo')==2
assert valor(203503200,'hijos')==3
assert valor(203503200,'estado civil')==2
assert valor(203503200,'pais')==0
assert valor(203503200,'a')==-1
