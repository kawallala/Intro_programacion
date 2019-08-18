#potencia: num int-> num
#potencia de la forma x^y con y un entero
#ej: potencia(2,4)->16
def potencia (a,b):
    t=1
    assert type(b)==int and b>=0
    if b==0:
        return 1
    else:
        t=t*a*potencia(a,b-1)
        return t
    

