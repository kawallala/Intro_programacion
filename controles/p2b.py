import p2a
#moda: int -> int
#cuenta que numero aparece mas veces en un numero entero positivo
#ej: moda(14540344554)==4
def moda(n,i=0,c=0,m=0):
    if i>9:
        return c
    if p2a.cuenta(i,n)>m:
        m=p2a.cuenta(i,n)
        c=i
        return moda(n,i+1,c,m)
    else:
        return moda(n,i+1,c,m)
    
    
