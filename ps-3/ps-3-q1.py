## Exercise 4.3 Part A
def f(x):
    return x * (x - 1)

def deri(f, x, d):
    return (f(x + d) - f(x)) / d

## Delta = 10^-2
d = 10**-2
approx_deri = deri(f, 1, d)

## The derivative of x(x-1) is 2x-1
true_deri = 2*1 - 1
print(f"True derivative: {true_deri}")
print(f"Numerical derivative with δ = {d}: {approx_deri}")

## The two values will not agree perfectly due to the approximation nature of the numerical method.

## Exercise 4.3 Part B
## Delta = 10^-4
d = 10**-4
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")

## Delta = 10^-6
d = 10**-6
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")

## Delta = 10^-8
d = 10**-8
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")

## Delta = 10^-10
d = 10**-10
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")

## Delta = 10^-12
d = 10**-12
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")


## Delta = 10^-14
d = 10**-14
approx_deri = deri(f, 1, d)
print(f"Numerical derivative with δ = {d}: {approx_deri}")
