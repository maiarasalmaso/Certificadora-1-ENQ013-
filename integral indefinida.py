import sympy as sp

print("\n=== INTEGRAL INDEFINIDA ===")

# Variável simbólica
x = sp.Symbol('x')

# Observações: as integrais indefinidas têm uma constante de integração C.

# Exemplo 1: ∫ cos(x) dx = sen(x) + C
f1 = sp.cos(x)
F1 = sp.integrate(f1, x)
print('\nExemplo 1: ∫ cos(x) dx')
print(f'Integrando: {f1} -> {F1} + C')
print(f'Verificação: d/dx({F1}) = {sp.diff(F1, x)}')

# Exemplo 2 (substituição): ∫ 2x*cos(x^2) dx = sen(x^2) + C
f2 = 2*x*sp.cos(x**2)
F2 = sp.integrate(f2, x)
print('\nExemplo 2: ∫ 2x*cos(x^2) dx (substituição u = x^2)')
print(f'Integrando: {f2} -> {F2} + C')
print(f'Verificação: d/dx({F2}) = {sp.diff(F2, x)}')