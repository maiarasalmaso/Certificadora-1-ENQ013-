from CoolProp.CoolProp import PropsSI

# --- Condições de Entrada ---
T = 298.15      # Temperatura em Kelvin (25°C)
P_atm = 101325  # Pressão atmosférica em Pascal (1 atm)
fluido = 'water'  # Fluido de interesse 

# --- Propriedades do Líquido Sub-resfriado (a T=25°C, P=1atm) ---

# 1. Densidade (do seu código)
rho = PropsSI('D', 'T', T, 'P', P_atm, fluido)

# 2. Capacidade Calorífica 
cp = PropsSI('C', 'T', T, 'P', P_atm, fluido)

# 3. Viscosidade Dinâmica 
# Símbolo 'V' v
mu = PropsSI('V', 'T', T, 'P', P_atm, fluido)

# 4. Condutividade Térmica
# Símbolo 'L' para (Lambda)
k = PropsSI('L', 'T', T, 'P', P_atm, fluido)

# --- Propriedades de Saturação (na curva de vapor, a T=25°C) 

# 5. Pressão de Saturação 
# (Usando Q=0 para "líquido saturado")
P_sat = PropsSI('P', 'T', T, 'Q', 0, fluido)

# 6. Entalpia do Vapor Saturado 
# (Usando Q=1 para "vapor saturado")
H_vap = PropsSI('H', 'T', T, 'Q', 1, fluido)

# 7. Entalpia do Líquido Saturado 
# (Usando Q=0 para "líquido saturado")
H_liq = PropsSI('H', 'T', T, 'Q', 0, fluido)

# 8. Calor Latente de Vaporização (ΔH_vap) 
# É a diferença entre a entalpia do vapor e do líquido saturados
delta_H_vap = H_vap - H_liq

# 9. Tensão Superficial 
# Símbolo 'I' para Surface Tension
sigma = PropsSI('I', 'T', T, 'Q', 0, fluido)


# --- Propriedades Adimensionais (Calculadas) ---

# 10. Número de Prandtl (calculado a partir das propriedades do líquido)
Pr = (cp * mu) / k


# --- Impressão dos Resultados ---
print(f"--- Propriedades da água a {T-273.15:.2f} °C ---")

print(f"\nPropriedades do Líquido (a P = {P_atm} Pa):")
print(f"  A densidade (ρ) é: \t\t{rho:.3f} kg/m³")
print(f"  Capacidade calorífica (cp) é: \t{cp:.3f} J/(kg·K)")
print(f"  Viscosidade dinâmica (μ) é: \t{mu:.6f} Pa·s")
print(f"  Condutividade térmica (k) é: \t{k:.4f} W/(m·K)")

print(f"\nPropriedades de Saturação (na curva de vapor):")
print(f"  A pressão de saturação (P_sat) é: \t{P_sat:.2f} Pa (ou {P_sat/1000:.3f} kPa)")
print(f"  Entalpia do vapor saturado (H_v) é: \t{H_vap:.2f} J/kg")
print(f"  Entalpia do líquido saturado (H_l) é: \t{H_liq:.2f} J/kg")
print(f"  Calor latente (ΔH_vap) é: \t\t{delta_H_vap:.2f} J/kg (ou {delta_H_vap/1000:.2f} kJ/kg)")
print(f"  Tensão superficial (σ) é: \t\t{sigma:.5f} N/m")

print(f"\nAdimensional (Líquido a {P_atm} Pa):")
print(f"  Número de Prandtl (Pr) é: \t\t{Pr:.3f}")
