from scipy.optimize import brent
import numpy as np

def f(x):
    return (x - 0.3)**2 * np.exp(x)

result_scipy = brent(f, brack=(0, 1))
print("Scipy method: ", result_scipy)

def brent_method(func, brack, tol=1.48e-8, maxiter=500):
    # Constants
    gr = (3 - np.sqrt(5)) / 2
    a, b = brack
    x = w = v = a + gr * (b - a)
    fw = fv = fx = func(x)
    d = e = 0.0

    for iter in range(maxiter):
        xm = 0.5 * (a + b)
        tol1 = tol * abs(x) + tol
        tol2 = 2.0 * tol1

        if abs(x - xm) <= (tol2 - 0.5 * (b - a)):
            return x

        if abs(e) > tol1:
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2 * (q - r)
            if q > 0:
                p = -p
            q = abs(q)
            etemp = e
            e = d

            if abs(p) >= abs(0.5 * q * etemp) or p <= q * (a - x) or p >= q * (b - x):
                e = a - x if x >= xm else b - x
                d = gr * e
            else:
                d = p / q
                u = x + d
                if u - a < tol2 or b - u < tol2:
                    d = np.sign(xm - x) * tol1
        else:
            e = a - x if x >= xm else b - x
            d = gr * e

        u = x + d if abs(d) >= tol1 else x + np.sign(d) * tol1
        fu = func(u)

        if fu <= fx:
            if u >= x:
                a = x
            else:
                b = x
            v, w, x = w, x, u
            fv, fw, fx = fw, fx, fu
        else:
            if u < x:
                a = u
            else:
                b = u
            if fu <= fw or w == x:
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu

    return x

manual_brent = brent_method(f, brack=(0, 1))
print("Manual implementation: ", manual_brent)
