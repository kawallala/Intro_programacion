#__L: list(str)
#__max: int
class Cola:
    #__init__: int -> list(None)
    #crea lista vacia, junto con el atributo del maximo numero de componentes permitidos en la lista
    #ej: c=Cola(3)
    def __init__(self, n):
        lista = []
        self.__L = lista
        self.__max = n
    #encolar: str -> bool
    #agrega el nombre de la persona al final de la lista, devuelve True al agregarlo correctamente
    #ej: c.append("x")-> True
    def encolar(self, x):
        assert type(x) == str
        if len(self.__L) + 1 <= self.__max:
            self.__L.append(x)
            return True
        return False
    #desencolar: None -> str
    #devuelve el nombre de la primera persona en la fila, sacandolo de la lista
    #ej: c=Cola(3);c.encolar("a");c.desencolar() -> "a"
    def desencolar(self):
        s = self.__L.pop(0)
        return s
    #contenido: None -> str
    #devuelve un string con los valores presentes en la Cola
    #ej: c.contenido() -> "a b c"
    def contenido(self):
        s = ""
        for i in self.__L[0:len(self.__L) - 1]:
            s = s + i + " "
        s = s + self.__L[len(self.__L) - 1]
        return s
    #largo: None -> int
    #devuelve el numero de integrantes en la cola
    #ej: c.largo() -> 3
    def largo(self):
        return len(self.__L)
    #esta_vacia: None-> bool
    #devuelve True si la lista esta vacia
    #ej: c=cola(3);c.esta_vacia -> True
    def esta_vacia(self):
        return self.__L == []
    #esta llena: None -> Bool
    #devuelve True si la lista esta llena(tiene el maximo permitido de valores
    #ej: c=cola(1);c.encolar("a");c.esta_llena() -> True
    def esta_llena(self):
        return len(self.__L) == self.__max

class TestCola:
    def __init__(self):
        self.__l = Cola(1)
    def test(self):
        assert self.__l.esta_vacia()
        assert not self.__l.esta_llena()
        self.__l.encolar("a")
        assert self.__l.contenido()=="a"
        assert self.__l.largo()==1
        assert self.__l.esta_llena()
TestCola().test()