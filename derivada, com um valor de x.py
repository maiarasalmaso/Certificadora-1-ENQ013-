
import math
import numpy as np



def numeric_derivative(func, x, h=1e-6):
    return (func(x + h) - func(x - h)) / (2 * h)


# Exemplo 1: f(x) = x**2 em x = 2
def f1(x):
    return x ** 2

valor_x = 2
deriv_num1 = numeric_derivative(f1, valor_x)
print(f"f(x) = x**2")
print(f"f'({valor_x}) ≈ {deriv_num1:.6f} (teórico = {2*valor_x})")
print()


# Exemplo 2: f(x) = sen(x) em x = pi/2
def f2(x):
    return math.sin(x)

valor_x2 = math.pi / 2
deriv_num2 = numeric_derivative(f2, valor_x2)
print(f"f(x) = sen(x)")
print(f"f'(π/2) ≈ {deriv_num2:.6f} (teórico = {math.cos(valor_x2):.6f})")
print()


# Exemplo 3: Derivada em vários pontos
def f3(x):
    return x ** 3 - 2 * x + 1

pontos = [-1, 0, 1, 2]
print(f"f(x) = x**3 - 2x + 1")
for ponto in pontos:
    deriv_valor = numeric_derivative(f3, ponto)

    # valor teórico 3x^2 - 2
    teorico = 3 * ponto ** 2 - 2
    print(f"f'({ponto}) ≈ {deriv_valor:.2f} (teórico = {teorico:.2f})")