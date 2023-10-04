def f(x):
    return x**4 - 2*x + 1

def trapezoidal_rule(func, a, b, N):
    h = (b - a) / N
    s = 0.5 * (func(a) + func(b))
    for i in range(1, N):
        s += func(a + i*h)
    return h * s

N1 = 10
N2 = 20
I1 = trapezoidal_rule(f, 0, 2, N1)
I2 = trapezoidal_rule(f, 0, 2, N2)


#Equation 5.28
estimated_error = (1/3) * (I1 - I2)
#Computed by hand
true_value = 4.4
true_error = abs(I2 - true_value)

print(f"Integral value with N1 = 10: {I1}")
print(f"Integral value with N2 = 20: {I2}")
print(f"Estimated error: {estimated_error}")
print(f"True error: {true_error}")
