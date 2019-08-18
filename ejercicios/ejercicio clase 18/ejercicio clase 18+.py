class Fraccion:
    # __init__:int int -> Fraccion
    # cra fraccion con numerador x y denominador y
    # devuelve referencia(direccion) a objeto
    # ej: Fraccion(1,2) -> referencia a objeto
    def __init__(self, x=0, y=1):
        if type(x) == str:
            i=x.find('/')
            self.__numerador=int(x[0:i])
            self.__denominador=int(x[i+1:])
        elif isinstance(x,Fraccion):
            self.__numerador=x.__numerador
            self.__denominador=x.__denominador
        else:
            self.__numerador=x
            self.__denominador=y
        assert self.__denominador!=0
    def getDenominador(self):
        return self.__denominador
    def getNumerador(self):
        return self.__numerador
    def mcd(self):
        a=self.__numerador
        b=self.__denominador
        if a<0:
            a=-a
        if b<0:
            b=-b
        while True:
            if a == 0 or b == 0 or a == b:
                break
            if a>b:
                a=a-b
            if b>a:
                b=b-a
        return max(a,b)
    def simplificar(self):
        m=self.mcd()
        a=self.getNumerador()
        b=self.getDenominador()
        return Fraccion(a/m,b/m)
    def aString(self):
        return str(self.__numerador)+"/"+str(self.__denominador)
    def __add__(self, other):
        a=self.__numerador*other.__denominador+other.__numerador*self.__denominador
        b=self.__denominador*other.__denominador
        f=Fraccion(a,b)
        return f.simplificar()
    def __sub__(self, other):
        a=Fraccion(-1)
        f=other*a
        return self+f
    def __mul__(self, other):
        a=self.__numerador*other.__numerador
        b=self.__denominador*other.__denominador
        f=Fraccion(a,b)
        return f.simplificar()
    def __div__(self, other):
        a=other.__numerador
        b=other.__denominador
        f=Fraccion(b,a)
        return self*f
    def __gt__(self, other):
        return self.__numerador*other.__denominador>other.__numerador*self.__denominador
    def __eq__(self, other):
        return self.__numerador*other.__denominador==other.__numerador*self.__denominador

print("Calculadora de Fracciones")
a=input("Fraccion 1(n/n)? ")
b=input("Fraccion 2(n/n)? ")
f1= Fraccion(a)
f2= Fraccion(b)
o=raw_input("Operacion (+ - * /)? ")
if o=="+":
    f=f1+f2
elif o=="-":
    f=f1-f2
elif o=="*":
    f=f1*f2
elif o=="/":
    f=f1/f2
print "Resultado= "+ f.aString()