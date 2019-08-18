#koch.py
import turtle

#fractal: int int ->None
#dibuja fractal de koch de nivel n y lado L
#ej: fractal(4,100)
def fractal(n,L):
    assert type(n)==int and n>=1
    assert type(L)==int and L>0
    lado(n,L)
    turtle.right(120)
    lado(n,L)
    turtle.right(120)
    lado(n,L)

#lado: int int -> None
#dibuja lado de fractal de koch
#ej:lado(4,100)
def lado(n,L,Lmin=6):
    assert type(n)==int and n>=1
    assert type(L)==int and L>0
    if n==1 or L<Lmin:
        turtle.forward(L)
    else:
        lado(n-1,L/3)
        turtle.left(60)
        lado(n-1,L/3)
        turtle.right(120)
        lado(n-1,L/3)
        turtle.left(60)
        lado(n-1,L/3)
fractal(4,200)