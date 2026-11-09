import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

# ---------------------------------------------------------------------------
# Diagrama de fases da água
# Eixo vertical: pressão em escala logarítmica (atm)
# Eixo horizontal: temperatura em escala esquemática (para separar 0,00 de 0,01)
# ---------------------------------------------------------------------------

# Constantes dos pontos notáveis
T_TRIPLO, P_TRIPLO = 0.01, 0.006          # ponto triplo
P_SOLIDIF = 1.00                          # solidificação convencional (0,00 °C)
T_EBULICAO, P_EBULICAO = 100.00, 1.00     # ebulição convencional
T_CRITICO, P_CRITICO = 373.99, 217.75     # ponto crítico

# Posições esquemáticas no eixo x
X_SOLID, X_TRIPLO, X_EBUL, X_CRIT = 0.0, 14.0, 232.0, 442.0


def x_temp(t):
    """Converte temperatura (°C) em coordenada x esquemática do gráfico."""
    t = np.asarray(t, dtype=float)
    x = np.empty_like(t)
    x[t <= 0] = t[t <= 0]
    m = (t > 0) & (t <= T_TRIPLO)
    x[m] = X_TRIPLO * t[m] / T_TRIPLO
    m = (t > T_TRIPLO) & (t <= T_EBULICAO)
    x[m] = X_TRIPLO + (X_EBUL - X_TRIPLO) * (t[m] - T_TRIPLO) / (T_EBULICAO - T_TRIPLO)
    m = t > T_EBULICAO
    x[m] = X_EBUL + (X_CRIT - X_EBUL) * (t[m] - T_EBULICAO) / (T_CRITICO - T_EBULICAO)
    return x


# --- Curva de sublimação (sólido-gás) --------------------------------------
T_sub = np.linspace(-45, T_TRIPLO, 400)
P_sub = P_TRIPLO * np.exp(-6140.0 * (1 / (T_sub + 273.15) - 1 / 273.16))

# --- Curva de fusão (sólido-líquido) ---------------------------------------
# Trecho entre o ponto triplo e a solidificação a 1 atm
P_fus_baixo = np.logspace(np.log10(P_TRIPLO), 0, 120)
T_fus_baixo = T_TRIPLO + (0 - T_TRIPLO) * (
    np.log10(P_fus_baixo) - np.log10(P_TRIPLO)) / (0 - np.log10(P_TRIPLO))
# Acima de 1 atm: inclinação negativa (comportamento anômalo da água)
P_fus_alto = np.logspace(0, np.log10(P_CRITICO), 200)
T_fus_alto = -0.03 * (P_fus_alto - 1)

# --- Curva de vaporização (líquido-gás) ------------------------------------
# Ajuste de Clausius-Clapeyron quadrático em 1/T passando pelos três pontos
T_vap = np.linspace(T_TRIPLO, T_CRITICO, 400)
u = 1.0 / (T_vap + 273.15)
coef = np.polyfit(
    [1 / 273.16, 1 / 373.15, 1 / 647.14],
    [np.log10(P_TRIPLO), np.log10(P_EBULICAO), np.log10(P_CRITICO)], 2)
P_vap = 10 ** np.polyval(coef, u)

# --- Figura ----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8))
x0, y0 = -75, 5e-4
X_MAX, Y_MAX = 560, 600

ax.plot(x_temp(T_sub), P_sub, color='black', linewidth=1.8)
ax.plot(x_temp(T_fus_baixo), P_fus_baixo, color='black', linewidth=1.8)
ax.plot(x_temp(T_fus_alto), P_fus_alto, color='black', linewidth=1.8)
ax.plot(x_temp(T_vap), P_vap, color='black', linewidth=1.8)

# Linhas pontilhadas de referência
ax.plot([x0, X_CRIT], [P_CRITICO, P_CRITICO], 'k:', linewidth=1.2)
ax.plot([x0, X_EBUL], [P_EBULICAO, P_EBULICAO], 'k:', linewidth=1.2)
ax.plot([x0, X_TRIPLO], [P_TRIPLO, P_TRIPLO], 'k:', linewidth=1.2)
ax.plot([X_SOLID, X_SOLID], [y0, P_SOLIDIF], 'k:', linewidth=1.2)
ax.plot([X_TRIPLO, X_TRIPLO], [y0, P_TRIPLO], 'k:', linewidth=1.2)
ax.plot([X_EBUL, X_EBUL], [y0, P_EBULICAO], 'k:', linewidth=1.2)
ax.plot([X_CRIT, X_CRIT], [y0, P_CRITICO], 'k:', linewidth=1.2)

# Pontos notáveis
X_FUS_TOPO = x_temp(T_fus_alto[-1])
ax.plot([X_SOLID, X_EBUL, X_TRIPLO, X_CRIT, X_FUS_TOPO],
        [P_SOLIDIF, P_EBULICAO, P_TRIPLO, P_CRITICO, P_CRITICO],
        'o', color='black', markersize=7, markeredgecolor='black')

# Rótulos das regiões
ax.text(-38, 8, 'Sólido', fontsize=18, ha='center')
ax.text(175, 40, 'Líquido', fontsize=18, ha='center')
ax.text(140, 0.003, 'Gás', fontsize=18, ha='center')

# Anotações dos pontos
ax.annotate('Ponto de\nsolidificação\nconvencional', xy=(X_SOLID, P_SOLIDIF),
            xytext=(-5, 0.08), fontsize=8.5, fontweight='bold',
            ha='right', va='center')
ax.annotate('Ponto de ebulição\nconvencional', xy=(X_EBUL, P_EBULICAO),
            xytext=(X_EBUL + 12, 0.30), fontsize=9, fontweight='bold',
            ha='left', va='center')
ax.annotate('Ponto\ntriplo', xy=(X_TRIPLO, P_TRIPLO),
            xytext=(X_TRIPLO + 12, 0.0022), fontsize=10, fontweight='bold',
            ha='left', va='center')
ax.annotate('Ponto\ncrítico', xy=(X_CRIT, P_CRITICO),
            xytext=(X_CRIT + 8, 300), fontsize=10, fontweight='bold',
            ha='left', va='center')

# Eixos em forma de seta
ax.annotate('', xy=(x0, Y_MAX), xytext=(x0, y0),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5))
ax.annotate('', xy=(500, y0), xytext=(x0, y0),
            arrowprops=dict(arrowstyle='->', color='black', linewidth=1.5))

# Escalas e rótulos dos eixos
ax.set_yscale('log')
ax.set_xlim(x0, X_MAX)
ax.set_ylim(y0, Y_MAX)
ax.set_xticks([X_SOLID, X_TRIPLO, X_EBUL, X_CRIT])
ax.set_xticklabels(['0,00', '0,01', '100,00', '373,99'], fontsize=11)
ax.set_yticks([P_TRIPLO, P_EBULICAO, P_CRITICO])
ax.set_yticklabels(['0,006', '1,00', '217,75'], fontsize=11)
ax.xaxis.set_minor_locator(NullLocator())
ax.yaxis.set_minor_locator(NullLocator())
ax.tick_params(axis='both', which='both', length=0)

ax.set_xlabel('Temperatura (°C)', fontsize=13, fontweight='bold')
ax.set_ylabel('Pressão (atm)', fontsize=13, fontweight='bold')
ax.set_title('Diagrama de Fases da Água', fontsize=20, fontweight='bold')

# Afasta os rótulos 0,00 e 0,01 para não se sobreporem
labels = ax.get_xticklabels()
labels[0].set_ha('right')
labels[1].set_ha('left')

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.savefig('diagrama-fase-agua.png', dpi=150)
plt.show()
