#mcd: int int -> int
#calcula el maximo comun divisor entre dos numeros enteros positivos
#ej: mcd(4,9)->1 (coprimos no primos)
#ej: mcd(2,4)->2 (pares)
#ej: mcd(3,6)->3 (impares multiplos de 3)
#ej: mcd(2,3)->1 (coprimos primos)
def mcd(x,y):
    assert type(x)==int and x>=0
    assert type(y)==int and y>=0
    a=max(x,y)
    b=min(x,y)
    if a%b==0: 
        return b
    else:
        return mcd(b,a%b)
assert mcd(4,9)==1
assert mcd(2,4)==2
assert mcd(3,6)==3
assert mcd(2,3)==1
