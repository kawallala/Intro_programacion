from conjunto import *
A=[]
B=[]
C=[]
archivo=open('A.txt')
for linea in archivo:
    A.append(linea.strip())
archivo.close()
archivo=open('B.txt')
for linea in archivo:
    B.append(linea.strip())
archivo.close
archivo=open('C.txt')
for linea in archivo:
    C.append(linea.strip())
archivo.close
TA=resta(A,union(B,C))
TB=resta(B,union(A,C))
TC=resta(C,union(A,B))
print 'alumnos que estan solo en un curso:'
print 'curso A: '+str(TA)
print 'curso B: '+str(TB)
print 'curso C: '+str(TC)