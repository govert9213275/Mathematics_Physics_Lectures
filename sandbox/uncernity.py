import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse
import matplotlib.gridspec as gridspec

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with multiple subplots
plt.figure(figsize=(15, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

# ------ EXAMPLE 1: BULL'S EYE DIAGRAM ------
ax1 = plt.subplot(gs[0, 0])

# Draw target rings
for r in [5, 4, 3, 2, 1]:
    circle = plt.Circle((0, 0), r, fill=False, edgecolor='black', linewidth=1)
    ax1.add_patch(circle)

# Generate four sets of shots with different error and uncertainty
scenarios = [
    {"name": "Mały błąd, mała niepewność", "offset": (0.5, 0.5), "uncertainty": 0.5, "color": "blue"},
    {"name": "Duży błąd, mała niepewność", "offset": (3.0, -1.0), "uncertainty": 0.5, "color": "red"},
    {"name": "Mały błąd, duża niepewność", "offset": (0.5, 0.5), "uncertainty": 2.0, "color": "green"},
    {"name": "Duży błąd, duża niepewność", "offset": (3.0, -1.0), "uncertainty": 2.0, "color": "purple"}
]

for scenario in scenarios:
    # Generate shots
    n_shots = 20
    x = np.random.normal(scenario["offset"][0], scenario["uncertainty"], n_shots)
    y = np.random.normal(scenario["offset"][1], scenario["uncertainty"], n_shots)
    
    # Calculate mean position
    mean_x, mean_y = np.mean(x), np.mean(y)
    
    # Plot shots
    ax1.scatter(x, y, color=scenario["color"], alpha=0.5, s=20, label=f"{scenario['name']}")
    ax1.scatter(mean_x, mean_y, color=scenario["color"], s=80, marker='x')
    
    # Draw uncertainty ellipse (2 sigma)
    ellipse = Ellipse((mean_x, mean_y), 
                     width=2*2*scenario["uncertainty"], 
                     height=2*2*scenario["uncertainty"],
                     edgecolor=scenario["color"], facecolor='none', 
                     alpha=0.7, linestyle='--')
    ax1.add_patch(ellipse)

# Plot true center
ax1.scatter(0, 0, color='black', s=100, marker='+', label='Prawdziwa wartość')

# Configure plot
ax1.set_xlim(-7, 7)
ax1.set_ylim(-7, 7)
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_title('Błąd i Niepewność w Strzelaniu do Tarczy', fontsize=14)
ax1.legend(loc='upper right', fontsize=8)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

# Add explanatory annotations
ax1.annotate("Średnie (x) pokazują błąd\nElipsy pokazują niepewność",
            xy=(0.05, 0.95), xycoords='axes fraction',
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7))

# ------ EXAMPLE 2: REPEATED MEASUREMENTS ------
ax2 = plt.subplot(gs[0, 1])

# Generate "true" data for a measurement
x_true = np.linspace(0, 10, 100)
y_true = 2 * x_true + 5

# Generate two sets of measurements with different error and uncertainty
x_low_error = np.linspace(0, 10, 10)
y_low_error = 2 * x_low_error + 5.5  # Small systematic error (+0.5)
y_low_error_noise = y_low_error + np.random.normal(0, 0.5, 10)  # Small uncertainty

x_high_error = np.linspace(0, 10, 10)
y_high_error = 2 * x_high_error + 8  # Large systematic error (+3)
y_high_error_noise = y_high_error + np.random.normal(0, 0.5, 10)  # Small uncertainty

x_low_uncertainty = np.linspace(0, 10, 10)
y_low_uncertainty = 2 * x_low_uncertainty + 5.5  # Small systematic error (+0.5)
y_low_uncertainty_noise = y_low_uncertainty + np.random.normal(0, 2.0, 10)  # Large uncertainty

x_high_uncertainty = np.linspace(0, 10, 10)
y_high_uncertainty = 2 * x_high_uncertainty + 8  # Large systematic error (+3)
y_high_uncertainty_noise = y_high_uncertainty + np.random.normal(0, 2.0, 10)  # Large uncertainty

# Plot data
ax2.plot(x_true, y_true, 'k-', linewidth=2, label='Prawdziwa wartość')
ax2.errorbar(x_low_error, y_low_error_noise, yerr=0.5, fmt='o', color='blue', 
             label='Mały błąd, mała niepewność', capsize=5)
ax2.errorbar(x_high_error, y_high_error_noise, yerr=0.5, fmt='o', color='red', 
             label='Duży błąd, mała niepewność', capsize=5)
ax2.errorbar(x_low_uncertainty, y_low_uncertainty_noise, yerr=2.0, fmt='o', color='green', 
             label='Mały błąd, duża niepewność', capsize=5)
ax2.errorbar(x_high_uncertainty, y_high_uncertainty_noise, yerr=2.0, fmt='o', color='purple', 
             label='Duży błąd, duża niepewność', capsize=5)

# Configure plot
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 35)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_title('Błąd i Niepewność w Pomiarach Liniowych', fontsize=14)
ax2.legend(loc='upper left', fontsize=8)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

# Add explanatory annotations
ax2.annotate("Odległość od prawdziwej linii = błąd\nSłupki błędów = niepewność",
            xy=(0.05, 0.95), xycoords='axes fraction',
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7))

# ------ EXAMPLE 3: DISTRIBUTION VIEW ------
ax3 = plt.subplot(gs[1, 0])

# Generate normal distributions with different means (errors) and std devs (uncertainties)
x = np.linspace(-10, 10, 1000)
true_value = 0

# Low error, low uncertainty
mean1 = 1
std1 = 1
y1 = np.exp(-0.5 * ((x - mean1) / std1) ** 2) / (std1 * np.sqrt(2 * np.pi))

# High error, low uncertainty
mean2 = 5
std2 = 1
y2 = np.exp(-0.5 * ((x - mean2) / std2) ** 2) / (std2 * np.sqrt(2 * np.pi))

# Low error, high uncertainty
mean3 = 1
std3 = 3
y3 = np.exp(-0.5 * ((x - mean3) / std3) ** 2) / (std3 * np.sqrt(2 * np.pi))

# High error, high uncertainty
mean4 = 5
std4 = 3
y4 = np.exp(-0.5 * ((x - mean4) / std4) ** 2) / (std4 * np.sqrt(2 * np.pi))

# Plot distributions
ax3.plot(x, y1, 'blue', linewidth=2, label='Mały błąd, mała niepewność')
ax3.plot(x, y2, 'red', linewidth=2, label='Duży błąd, mała niepewność')
ax3.plot(x, y3, 'green', linewidth=2, label='Mały błąd, duża niepewność')
ax3.plot(x, y4, 'purple', linewidth=2, label='Duży błąd, duża niepewność')

# Mark true value and means
ax3.axvline(x=true_value, color='black', linestyle='-', linewidth=2, label='Prawdziwa wartość')
ax3.axvline(x=mean1, color='blue', linestyle='--', linewidth=1)
ax3.axvline(x=mean2, color='red', linestyle='--', linewidth=1)
ax3.axvline(x=mean3, color='green', linestyle='--', linewidth=1)
ax3.axvline(x=mean4, color='purple', linestyle='--', linewidth=1)

# Add shaded regions for uncertainty
for mean, std, color in [(mean1, std1, 'blue'), (mean2, std2, 'red'), 
                         (mean3, std3, 'green'), (mean4, std4, 'purple')]:
    ax3.axvspan(mean - std, mean + std, alpha=0.2, color=color)

# Configure plot
ax3.set_xlim(-10, 10)
ax3.set_ylim(0, 0.45)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_title('Rozkłady Prawdopodobieństwa: Błąd vs Niepewność', fontsize=14)
ax3.legend(loc='upper right', fontsize=8)
ax3.set_xlabel('Wartość')
ax3.set_ylabel('Gęstość prawdopodobieństwa')

# Add explanatory annotations
ax3.annotate("Odległość od prawdziwej wartości = błąd\nSzerokość rozkładu = niepewność",
            xy=(0.05, 0.95), xycoords='axes fraction',
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7))

# ------ EXAMPLE 4: ERROR PROPAGATION ------
ax4 = plt.subplot(gs[1, 1])

# Create a grid for contour plot
x = np.linspace(8, 12, 100)  # x = 10 ± 2
y = np.linspace(4, 8, 100)   # y = 6 ± 2
X, Y = np.meshgrid(x, y)

# Calculate z = x*y (with true values x=10, y=6, so z=60)
Z = X * Y

# Calculate the gradient at the true values
dx_dz = 6  # dz/dx = y = 6
dy_dz = 10  # dz/dy = x = 10

# Draw contour plot
contour = ax4.contour(X, Y, Z, levels=[40, 50, 60, 70, 80], colors='black', alpha=0.7)
ax4.clabel(contour, inline=True, fontsize=8)
contourf = ax4.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.5)

# Mark true values
ax4.scatter(10, 6, color='red', s=100, marker='+', label='Prawdziwa wartość (x=10, y=6)')

# Draw error rectangles
small_error_rect = Rectangle((9.5, 5.5), 1, 1, linewidth=2, 
                            edgecolor='blue', facecolor='none', label='Mały błąd')
large_error_rect = Rectangle((8, 4), 4, 4, linewidth=2,
                            edgecolor='red', facecolor='none', label='Duży błąd')
ax4.add_patch(small_error_rect)
ax4.add_patch(large_error_rect)

# Configure plot
ax4.set_xlim(7, 13)
ax4.set_ylim(3, 9)
ax4.grid(True, linestyle='--', alpha=0.7)
ax4.set_title('Propagacja Błędu i Niepewności: z = x * y', fontsize=14)
ax4.legend(loc='upper right', fontsize=8)
ax4.set_xlabel('x')
ax4.set_ylabel('y')

# Add colorbar
cbar = plt.colorbar(contourf, ax=ax4)
cbar.set_label('z = x * y')

# Add explanatory annotations
ax4.annotate("Prostokąty pokazują zakres niepewności\nKolory pokazują jak błędy się propagują",
            xy=(0.05, 0.95), xycoords='axes fraction',
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7))

# ------ OVERALL FIGURE SETTINGS ------
plt.suptitle('Różnica między Błędem a Niepewnością', fontsize=16, y=0.98)

# Add explanatory note at the bottom
explanation = """
BŁĄD (ERROR): Różnica między zmierzoną wartością a prawdziwą wartością. Może być systematyczny (stały offset) lub losowy.
NIEPEWNOŚĆ (UNCERTAINTY): Zakres wartości, w którym prawdopodobnie leży prawdziwa wartość. Miara naszego braku wiedzy o dokładnej wartości.

Łatwo zapamiętać: Błąd mówi JAK DALEKO od prawdy jesteśmy. Niepewność mówi JAK PEWNI jesteśmy swojego wyniku.
"""

plt.figtext(0.5, 0.01, explanation, wrap=True, horizontalalignment='center', fontsize=12, 
           bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.5))

plt.tight_layout()
plt.subplots_adjust(bottom=0.12)
plt.savefig('error_vs_uncertainty_plots.png', dpi=300, bbox_inches='tight')
plt.show()