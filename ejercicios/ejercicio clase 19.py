class Cola:
    def __init__(self):
        self.__L=[]
    def getlista(self):
        return self.__L
    def vacia(self):
        return self.getlista()==[]
    def vaciar(self):
        self.__L=[]
    def poner(self,x):
        self.__L.append(x)
    def sacar(self):
        return self.__L.pop(0)

class TestCola:
    def __init__(self):
        self.__1=Cola()
    def test(self):
        self.__1.poner(1)
        assert self.__1.getlista()==[1]
        assert not self.__1.vacia()
        self.__1.sacar()
        assert self.__1.getlista()==[]
        self.__1.poner(5)
        self.__1.vaciar()
        assert self.__1.getlista()==[]
TestCola().test()