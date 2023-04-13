def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """
    Implementação do método da bisseção para encontrar a raiz da função f no intervalo [a,b].
    tol é a tolerância desejada e max_iter é o número máximo de iterações permitidas.
    """
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        raise ValueError("Os valores de f(a) e f(b) devem ter sinais opostos!")
    for i in range(max_iter):

        c = (a + b)/2
        fc = f(c)
        errado = b - a
        print(f'{a:<25} |{b:<25} |{c:<25} |{abs(fc):<20} |{(errado):<25} ')
        if abs(fc) < tol:
            return c
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    raise ValueError("O método da bisseção não convergiu após {} iterações!".format(max_iter))

from numpy import log
from numpy import log as ln
from math import exp
from math import e
from math import sin
from math import cos

def f(x):
    # return 0.25*x**(3)-5.876*x**(2)+5.306*x -45.89
    #  return 2*ln(3-cos(x))-3*x**(x) +(5*sin(x))

      return -0.8*x**(3)+1.994*x**(2)+20.01*x-9.86
    #  return 4*sin(x)-e**(x)
    # return 2**(x) - 4*x
    #return -(30/ln(x)) + 2*x + 10
    #  return ( ((exp(1))**x) + ((ln(x))**(-1)) - 10 )
    
a = 
b = 0.5
tol = 1e-5
max_iter = 100
print(f'{"a":<25} |{"b":<25} |{"Xm":<25} |{"F(x)":<20} |{"E":<25} ')

raiz = bissecao(f, a, b, tol, max_iter)
print("A raiz é:", raiz)


