def corda(f, a, b, tol=1e-6, max_iter=100):
    """
    Implementação do método da corda para encontrar a raiz da função f no intervalo [a,b].
    tol é a tolerância desejada e max_iter é o número máximo de iterações permitidas.
    """
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        raise ValueError("Os valores de f(a) e f(b) devem ter sinais opostos!")
    for i in range(max_iter):
        c = a - (f(a)*(b - a))/(f(b) - f(a))
        fc = f(c)
        errado = b - c
        print(f'{i} |{c:<25} |{fc:<25} |{(errado):<25} ')
        if abs(fc) < tol:
            return c
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    raise ValueError("O método da corda não convergiu após {} iterações!".format(max_iter))
from numpy import log as ln
from math import exp
from math import e 
from math import sin

def f(x):

    # return 0.25*x**(3)-5.876*x**(2)+5.306*x -45.89
    # return 0.1*x**(3)-ℯ**(2*x)+2
    return -0.8*x**(3)+1.994*x**(2)+20.01*x-9.86
    #return 4*sin(x)-e**(x)

    #return 2**(x) - 4*x
    #return 1.4*(x**3) - 2.71*(x**2) - 4.035*x + 5.9404
    # return -(30/ln(x)) + 2*x + 10
    # return ( ((exp(1))**x) + ((ln(x))**(-1)) - 10 )

#a = 0.98
#b = 2.2
a = 6.18
b = 6.22
tol = 1e-5
max_iter = 100
print(f'{"i"} |{"Xi":<25} |{"F(Xn)":<25} |{"E":<25} ')


raiz = corda(f, a, b, tol, max_iter)
print("A raiz é:", raiz)
