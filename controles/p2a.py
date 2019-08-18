#cuenta: int int -> int
#cuenta el numero de veces que aparece el numero i en el entero positivo n
#ej: cuenta(5,12451245) -> 2
#ej: cuenta(2,1)-> 0
#ej: cuenta(2,22222)->5
def cuenta(i,n,c=0):
    assert type(i)==int and type(n)==int
    if n==0:
        return c
    else:
        if n%10==i:
            return cuenta(i,n/10,c+1)
        else:
            return cuenta(i,n/10,c)
assert cuenta(5,12451245)==2
assert cuenta(2,1)==0
assert cuenta(2,22222)==5
