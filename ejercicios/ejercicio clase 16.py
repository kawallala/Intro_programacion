import random
A=[]
L=[3,4,2,5]
for i in range(100000):
    L.append(random.randint(0,100000))

#quicksort: list int int -> None
#ordena L entre indices ip e iu
#ej: quicksort(lista,0,len(lista)-1)

def quicksort(L,ip,iu):
  #caso base(1 elemento)
	if ip>=iu: return

  #particionar (y obtener indice de pivote)
	i=particionar(L,ip,iu)

  #ordenar 1 parte
	quicksort(L,ip,i-1)

  #ordenar 2 parte
	quicksort(L,i+1,iu)

#particionar: list int int -> int
#particiona L entre ip e iu (devuelve indice de pivote)
#ej: particionar(lista,0,len(lista)-1)

def particionar(L,ip,iu):
  #elegir pivote (por ejemplo: el primero)
  pivote=L[ip]
  #repetir hasta que indices se superen
  i=ip; j=ip+1 #indices para menores y mayores/iguales
  while j<=iu:
     while j<=iu and L[j]>=pivote: j+=1
     while j<=iu and L[j]<pivote:
         L.insert(i+1,L[j])
         L.pop(j+1)
         i+=1; j+=1
  #pivote a su posicion final
  L[ip]=L[i]
  L[i]=pivote
  return i

quicksort(L,0,len(L)-1)
print L