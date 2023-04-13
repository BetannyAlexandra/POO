def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Implementação do método de Newton para encontrar a raiz da função f.
    df é a derivada da função f, x0 é a aproximação inicial, tol é a tolerância desejada
    e max_iter é o número máximo de iterações permitidas.
    """
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - fx/dfx
        errado = x1 - x0
        print(f'{i} |{x1:<25} |{x0:<25} |{(errado):<25} ')
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("O método de Newton não convergiu após {} iterações!".format(max_iter))

def f(x):
    return x**2 - 4

def df(x):
    return 2*x

x0 = 1
tol = 1e-5
max_iter = 100

raiz = newton(f, df, x0, tol, max_iter)
print("A raiz é:", raiz)
