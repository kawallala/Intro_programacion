#valido: int int -> bool
#determina si un numero entero no negativo esta escrito en la base correcta entre 2 y 10
#ej: valido(102,3) -> True
#ej: valido(102,2) -> False
def valido(a,b):
    assert type(a)==int and a>=0
    assert type(b)==int and b>=2 and b<=10
    if (a%10)<b:
        if a/10 ==0:
            return True
        else:
            return valido(a/10,b)
    else:
        return False
assert valido(102,3)==True
assert valido(102,2)==False


#decimal: int int -> int
#transforma un numero a entero positivo de base b a un decimal
#ej decimal(215,8)->141
#ej decimal(1,6) ->1
def decimal(a,b,i=0):
    assert type(a)==int and a>=0
    assert type(b)==int and b>=2 and b<=10
    assert valido(a,b)==True
    if a/10==0:
        return a*b**i
    else:
        return (a%10)*b**i+decimal(a/10,b,i+1)
assert decimal(215,8)==141
assert decimal(1,6)==1


#numero: int int -> int
#convierte un numero entero decimal 'a' a otro escrito en una base b entre 2 y 10
#ej: numero(431,8) -> 657
#ej:numero(1,2)->1
#ej:numero(12345678,9)->25206070
def numero(a,b,i=0):
    assert type(a)==int and a>=0
    assert type(b)==int and b>=2 and b<=10
    if a/b==0:
        return (a%b)*10**i
    else:
        return (a%b)*10**i+numero(a/b,b,i+1)
assert numero(431,8)==657
assert numero(1,2)==1
assert numero(12345678,9)==25206070

#digitos: int -> int
#calcula los digitos de un numero
#ej digitos(1)->1
#ej digitos(101)->3
def digitos(x,i=0):
    assert type(x)==int
    if x/10==0:
        return i+1
    else:
        return digitos(x/10,i+1)
assert digitos(1)==1
assert digitos(101)==3

#primero: int-> int
#devuelve el primer digito de un numero
#ej primero(5)->5
#ej primero(123)->1
def primero(x):
    if x/10==0:
        return x
    else:
        return primero(x/10)
assert primero(5)==5
assert primero(123)==1

#ultimos: int-> int
#devuelve el numero sin el primer digito
#ej ultimos(5)->5
#ej ultimos(123)->23
def ultimos(x):
    if x/10==0:
        return x
    else:
        return x%(10**(digitos(x)-1))
assert ultimos(5)==5
assert ultimos(123)==23

