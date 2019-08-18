from Tkinter import *
from time import time


# __L: list(str)
# __max: int
class Cola:
    # __init__: int -> list(None)
    # crea lista vacia, junto con el atributo del maximo numero de componentes permitidos en la lista
    # ej: c=Cola(3)
    def __init__(self, n):
        lista = []
        self.__L = lista
        self.__max = n

    # encolar: str -> bool
    # agrega el nombre de la persona al final de la lista, devuelve True al agregarlo correctamente
    # ej: c.append("x")-> True
    def encolar(self, x):
        assert type(x) == str
        if len(self.__L) + 1 <= self.__max:
            self.__L.append(x)
            return True
        return False

    # desencolar: None -> str
    # devuelve el nombre de la primera persona en la fila, sacandolo de la lista
    # ej: c=Cola(3);c.encolar("a");c.desencolar() -> "a"
    def desencolar(self):
        s = self.__L.pop(0)
        return s

    # contenido: None -> str
    # devuelve un string con los valores presentes en la Cola
    # ej: c.contenido() -> "a b c"
    @property
    def contenido(self):
        s = ""
        if not self.__L:
            return s
        for i in self.__L[0:len(self.__L) - 1]:
            s = s + i + " "
        s = s + self.__L[len(self.__L) - 1]
        return s

    # largo: None -> int
    # devuelve el numero de integrantes en la cola
    # ej: c.largo() -> 3
    def largo(self):
        return len(self.__L)

    # esta_vacia: None-> bool
    # devuelve True si la lista esta vacia
    # ej: c=cola(3);c.esta_vacia -> True
    def esta_vacia(self):
        return self.__L == []

    # esta llena: None -> Bool
    # devuelve True si la lista esta llena(tiene el maximo permitido de valores
    # ej: c=cola(1);c.encolar("a");c.esta_llena() -> True
    def esta_llena(self):
        return len(self.__L) == self.__max


class TestCola:
    def __init__(self):
        self.__l = Cola(1)

    def test(self):
        assert self.__l.esta_vacia()
        assert not self.__l.esta_llena()
        self.__l.encolar("a")
        assert self.__l.contenido == "a"
        assert self.__l.largo() == 1
        assert self.__l.esta_llena()


TestCola().test()

T = int(time())
L1 = Cola(5)
L2 = Cola(10)
L1T = Cola(5)
L2T = Cola(10)


def actureloj(x):
    t = int(x) - T
    reloj.config(text="Reloj=" + str(t))


def agregar1(x):
    s = c1.get()
    if L1.encolar(s):
        L1T.encolar(str((int(time()) - T)))
        clientes1.config(text=L1.contenido)
        Largo1.config(text=str(L1.largo()))
        c1.delete(0, END)
        actureloj(time())
    else:
        c1.delete(0, END)
        c1.insert(0, "cola llena")


def agregar2(x):
    s = c2.get()
    if L2.encolar(s):
        L2T.encolar(str((int(time()) - T)))
        clientes2.config(text=L2.contenido)
        Largo2.config(text=str(L2.largo()))
        c2.delete(0, END)
        actureloj(time())
    else:
        c2.delete(0, END)
        c2.config(text="cola llena")
        c2.insert(0, "cola llena")


def caja():
    c1.delete(0, END)
    c2.delete(0, END)
    if not L1.esta_vacia():
        n = L1.desencolar()
        t = (int(time()) - T) - int(L1T.desencolar())
        sgdos.config(text="sgdos que espero: " + str(t))
        a = L1.contenido
        clientes1.config(text=a)
        Largo1.config(text=str(L1.largo()))
        atendiendo.config(text="atendiendo a: " + n)
        actureloj(time())
    elif L1.esta_vacia() and L2.esta_vacia():
        clientes1.config(text="agrege clientes")
        actureloj(time())
    else:
        n = L2.desencolar()
        t = (int(time()) - T) - int(L2T.desencolar())
        sgdos.config(text="sgdos que espero: " + str(t))
        a = L2.contenido
        clientes2.config(text=a)
        Largo2.config(text=str(L2.largo()))
        atendiendo.config(text="atendiendo a: " + n)
        actureloj(time())


v = Tk()
F = Frame(v)
f1 = Frame(v)
f2 = Frame(v)
f3 = Frame(v)
f4 = Frame(v)
caja = Button(F, text="caja", width=20, command=caja)
caja.pack(side=LEFT)
atendiendo = Label(F, text="atendiendo a nadie", width=20)
atendiendo.pack(side=LEFT)
sgdos = Label(F, text="sgdos que espero: 0", width=20)
sgdos.pack(side=LEFT)
reloj = Label(F, text="Reloj=0", width=20)
reloj.pack(side=LEFT)
cola = Label(f1, text="cola", width=20).pack()
cola1 = Label(f1, text="cola1", width=20).pack()
cola2 = Label(f1, text="cola2", width=20).pack()
clientes = Label(f2, text="Clientes en cola", width=20).pack()
clientes1 = Label(f2, text="", width=20)
clientes1.pack()
clientes2 = Label(f2, text="", width=20)
clientes2.pack()
Largo = Label(f3, text="Largo cola", width=20).pack()
Largo1 = Label(f3, text="0", width=20)
Largo1.pack()
Largo2 = Label(f3, text="0", width=20)
Largo2.pack()
cliente = Label(f4, text="Cliente que llega", width=20).pack()
c1 = Entry(f4, width=20)
c1.pack()
c1.bind("<Return>", agregar1)
c2 = Entry(f4, width=20)
c2.pack()
c2.bind("<Return>", agregar2)
F.pack()
f1.pack(side=LEFT)
f2.pack(side=LEFT)
f3.pack(side=LEFT)
f4.pack()

v.mainloop()
