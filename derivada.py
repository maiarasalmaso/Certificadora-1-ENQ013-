import sympy as sp

x = sp.Symbol('x')

# Função composta: f(g(x)) = sen(x²)
f = sp.sin(x**2)

derivada = sp.diff(f, x)
print(f"f(x) = sen(x²)")
print(f"f'(x) = {derivada}")
