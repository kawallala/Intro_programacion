import potencia
#potenciasDe2: none -> none
#calculo recursivo de las potencias de 2
#ej: pot2()
def potenciasDe2():
    b=input('potencia?')
    if b<0 : return
    print '2**'+str(b)+'=',potencia.potencia(2,b)
    potenciasDe2()
