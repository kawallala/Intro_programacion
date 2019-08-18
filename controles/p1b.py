import p1
#muj: None -> int
#determina la cantidad de mujeres chilenas solteras menores que 18, a partir de una lista de numeros
#ej: muj() -> 6
def muj(suma=0):
    a=input('persona? ')
    if a==0:
        print 'la cantidad de mujeres solicitadas es', suma
        return
    if p1.valor(a,'sexo')==2 and p1.valor(a,'edad')<18 and p1.valor(a,'estado civil')==1 and p1.valor(a,'pais')==0 and p1.valor(a,'hijos')>=1:
        muj(suma+1)
    else:
        muj(suma)
