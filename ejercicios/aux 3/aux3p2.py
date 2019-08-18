from aux3 import *
#lista: valor(Tiempo) siguiente(lista)
estructura.crear("lista", "valor siguiente")

#def mayorTiempo: lista -> Tiempo
#entrega el valor mayor de tiempo de la lista
#ej mayorTiempo(lista(Tiempo(1,30),lista(Tiempo(0,30),None))) -> Tiempo(1,30)
def mayorTiempo(x,mayor=0):
    assert type(x)==lista or x==None
    if x==None:
        return mayor
    t=enMinutos(x.valor)
    if t>mayor:
        mayor=t
        return mayorTiempo(x.siguiente,mayor)
    else:
        return mayorTiempo(x.siguiente,mayor)

#promedioTiempos: lista -> Tiempo
#retorna el promedio de una lista de Tiempos

def promedioTiemo(x,suma=0,n=0):
    if L==None:
        return Tiempo((suma/n)/60,(suma/n)%60)
    suma=suma+enMinutos(x.valor)
    return promedioTiempos(x.siguiente,suma,n+1)

#cuentaMenors
    
