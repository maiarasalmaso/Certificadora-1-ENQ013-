import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parâmetros do problema
U = 30.0  # Coeficiente global de transferência de calor (J/s·m²·°C)
A = 40.0  # Área de troca térmica (m²)
V = 10.0  # Volume do tanque (m³)
rho = 1000.0  # Densidade (kg/m³)
cp = 4184.0  # Calor específico (J/kg·°C)
T_env = 15.0  # Temperatura ambiente (°C
T0 = 20.0  # Temperatura inicial (°C)
vazao = 2.0  # Vazão volumétrica (m³/h)
T_in = 50.0  # Temperatura de entrada (°C)

# Converter vazão para m³/s
vazao_s = vazao / 3600.0

# Equação diferencial do balanço de energia
def tank_temperature(t, T):
    # dT/dt = (1/V) * [vazao*T_in - vazao*T - (U*A/(rho*cp))*(T - T_env)]
    dTdt = (1/V) * (vazao*T_in - vazao*T) - (U*A/(rho*cp*V)) * (T - T_env)
    return dTdt

# Tempo de simulação (0 a 10 horas)
t_span = (0, 60)
t_eval = np.linspace(0, 60, 1000)

# Resolver a EDO
sol = solve_ivp(tank_temperature, t_span, [T0], t_eval=t_eval, method='RK45')

# Calcular temperatura em estado estacionário
# No estado estacionário: dT/dt = 0
# 0 = vazao*T_in - vazao*T_ss - (U*A/(rho*cp))*(T_ss - T_env)
T_ss = (vazao*T_in + (U*A/(rho*cp))*T_env) / (vazao + U*A/(rho*cp))

print(f"Temperatura inicial: {T0:.2f} °C")
print(f"Temperatura em estado estacionário: {T_ss:.2f} °C")

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b-', linewidth=2, label='Temperatura do tanque')
plt.xlabel('Tempo (horas)')
plt.ylabel('Temperatura (°C)')
plt.title('Evolução da Temperatura no Tanque Não Isolado\n(Exemplo 3.4)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(10, 55)
plt.show()

# Análise adicional
print("\n=== ANÁLISE DO SISTEMA ===")
print(f"Taxa de entrada de calor pelo fluido: {vazao*rho*cp*T_in/1e6:.2f} MJ/h")
print(f"Taxa de perda de calor máxima: {U*A*(T_ss-T_env)/3600:.2f} J/s")
print(f"Constante de tempo do sistema: {V/vazao:.2f} horas")

# Verificar balanço de energia em estado estacionário
entrada_energia = vazao * rho * cp * T_in
saida_fluido = vazao * rho * cp * T_ss
perda_calor = U * A * (T_ss - T_env) * 3600  # Convertendo para J/h

print(f"\nBalanço em estado estacionário:")
print(f"Energia que entra: {entrada_energia/1e6:.2f} MJ/h")
print(f"Energia que sai pelo fluido: {saida_fluido/1e6:.2f} MJ/h")
print(f"Perda por convecção: {perda_calor/1e6:.2f} MJ/h")
print(f"Diferença (deve ser ~0): {(entrada_energia - saida_fluido - perda_calor)/1e6:.3f} MJ/h")