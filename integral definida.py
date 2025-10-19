import sympy as sp

# Exemplo 1: Integral definida básica
print("=== EXEMPLO 1: Integral de x² de 0 a 2 ===")

# Definir a variável simbólica
x = sp.Symbol('x')

# Definir a função
funcao = x**2

# Calcular a integral definida
integral = sp.integrate(funcao, (x, 0, 2))
print(f"∫₀² x² dx = {integral}")
print(f"Valor numérico: {integral.evalf()}")
print()

# Exemplo 2: Integral com função trigonométrica
print("=== EXEMPLO 2: Integral de sen(x) de 0 a π ===")

funcao2 = sp.sin(x)
integral2 = sp.integrate(funcao2, (x, 0, sp.pi))
print(f"∫₀^π sen(x) dx = {integral2}")
print(f"Valor numérico: {integral2.evalf()}")
print()

# Exemplo 3: Integral mais complexa
print("=== EXEMPLO 3: Integral de e^x de 0 a 1 ===")

funcao3 = sp.exp(x)
integral3 = sp.integrate(funcao3, (x, 0, 1))
print(f"∫₀¹ e^x dx = {integral3}")
print(f"Valor numérico: {integral3.evalf()}")
print()

# Exemplo 4: Visualização gráfica 
try:
    import matplotlib.pyplot as plt
    import numpy as np
    
    print("=== EXEMPLO 4: Visualização gráfica ===")
    
    # Criar dados para plotagem
    x_vals = np.linspace(0, 2, 100)
    y_vals = x_vals**2
    
    # Plotar a função
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = x²')
    
    # Preencher a área sob a curva
    plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue')
    
    # Configurações do gráfico
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Área sob a curva: ∫₀² x² dx = {integral}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
except ImportError:
    print("Matplotlib não instalado. Para visualização gráfica, instale: pip install matplotlib")