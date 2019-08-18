import estructura
#Tiempo: horas(int) minutos(int)
estructura.crear('Tiempo', 'horas minutos')

#def esTiempo: Tiempo -> Bool
#determina si un valor esta escrito en Tiempo
#ej: esTiempo(Tiempo(2,20)) -> True
def esTiempo(x):
    if type(x) == Tiempo:
        h=x.horas
        m=x.minutos
        return 0<=h<=24 and 0<=m<=59
    else:
        return False
assert esTiempo(Tiempo(2,20))==True

#def aString: Tiempo -> str
#da el string de un tiempo de la forma HH:MM
#ej: aString(Tiempo(2,20))-> 2:20
def aString(x):
    assert esTiempo(x)
    return str(x.horas)+':'+str(x.minutos)
assert aString(Tiempo(2,20))=='2:20'

#def: enMinutos: Tiempo -> int
#da el tiempo solo en minutos
#ej: enMinutos(Tiempo(1,30)) -> 90
def enMinutos(x):
    assert esTiempo(x)
    return x.horas*60+x.minutos
assert enMinutos(Tiempo(1,30))==90

#def sumar: Tiempo Tiempo -> Tiempo
#suma dos tiempos
#ej: suma(Tiempo(5,0),Tiempo(5,0)) -> Tiempo(10,0)
def suma(x,y):
    assert esTiempo(x) and esTiempo(y)
    a=enMinutos(x)
    b=enMinutos(y)
    t=a+b
    return Tiempo(t/60,t%60)
assert suma(Tiempo(5,0),Tiempo(5,0))==Tiempo(10,0)

#def restar: Tiempo Tiempo -> Tiempo
#resta dos tiempos
#ej: resta(Tiempo(5,0),Tiempo(5,0)) -> Tiempo(0,0)
def resta(x,y):
    assert esTiempo(x) and esTiempo(y)
    a=enMinutos(x)
    b=enMinutos(y)
    t=a-b
    if t>=0:
        return Tiempo(t/60,t%60)
    else:
        t=1440+t
        return Tiempo(t/60,t%60)
assert resta(Tiempo(5,0),Tiempo(5,0))==Tiempo(0,0)

#def comparar: Tiempo Tiempo -> int
#compara dos tiempos y entrega 0 1 -1 dependiendo del caso
#ej: comparar(Tiempo(1,30),Tiempo(0,30)) ->1
def comparar(x,y):
    assert esTiempo(x) and esTiempo(y)
    a=enMinutos(x)
    b=enMinutos(y)
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1
assert comparar(Tiempo(1,30),Tiempo(0,30))==1

def programa(mayor=0,suma=0,n=0):
    a=input('hora de la forma HHMM')
    if a==0:
        print 'mayor:', aString(Tiempo(mayor/60,mayor%60))
        print 'suma', str(suma)
        print 'promedio', str(suma/n)
    t=Tiempo(a/100,a%100)
    if enMinutos(t)>mayor:
        mayor=enMinutos(t)
    suma=suma+enMinutos(t)
    programa(mayor,suma,n+1)
