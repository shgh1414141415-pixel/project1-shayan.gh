
import sympy as sp

x = sp.symbols('x')

f_expr = sp.sympify(input("Enter f(x): "))
df_expr = sp.diff(f_expr, x)

f = sp.lambdify(x, f_expr, "math")
df = sp.lambdify(x, df_expr, "math")

n = float(input("Enter initial guess: "))
error = 1

while error > 0.00001:
    nnew = n - f(n) / df(n)
    error = abs(nnew - n)
    n = nnew

print("Answer:", n)
