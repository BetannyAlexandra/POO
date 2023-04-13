def bisection(f,a,b,eps):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print("Error: function has the same sign in both extremes")
        exit(0)
    while b-a > eps:
        c = (a+b)/2.
        fc = f(c)
        if fa*fc < 0:
            b, fb = c, fc
        elif fa*fc > 0:
            a, fa = c, fc
        else:
            return c
    return (a+b)/2.

if __name__ == "__main__":
    def f(x):
        return (2**x)-2*x
print(bisection(f,0.,1.,1.e-6))
