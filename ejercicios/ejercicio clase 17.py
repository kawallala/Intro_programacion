nombre=raw_input('nombre de archivo?')
A=open(nombre+'.txt','r')
s=0
for linea in A:
    d=linea.strip()
    s=len(d)+s
print s
