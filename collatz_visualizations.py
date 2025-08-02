"""
Collatz Spectral Visualization Toolkit
Author: Badr Elsayed
Affiliation: Al-Azhar University
Date: August 2025

This script generates three visualizations for the paper:
"Collatz Spectral Dynamics and the Mean-Square Vanishing of the Zeta Tail"

Includes:
1. Basic spectral decay plot
2. Clean error vs t plot
3. Log-log regression of spectral error
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# DATA SHARED ACROSS PLOTS
# =========================
t_values = [100, 500, 1000, 5000, 8000, 10000]
E_squared = [0.382, 0.157, 0.088, 0.021, 0.012, 0.009]

# =========================
# PLOT 1: mean_square_error.png
# =========================
def plot_mean_square_error():
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, E_squared, marker='o', linewidth=2, label=r'$|E(1/2 + it)|^2$')
    plt.axhline(0, color='red', linestyle='--')
    plt.title("Mean-Square Error Decay on Critical Line")
    plt.xlabel(r"$t$")
    plt.ylabel(r"$|E(1/2 + it)|^2$")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("mean_square_error.png", dpi=300)
    plt.close()

# =========================
# PLOT 2: zeta_spectrum_collatz.png
# =========================
def plot_raw_error_vs_t():
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, E_squared, marker='o', linestyle='-', color='blue', label=r'$|E(1/2 + it)|^2$')
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'$|E(1/2 + it)|^2$', fontsize=14)
    plt.title('Mean-Square Spectral Error on Critical Line', fontsize=16)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("zeta_spectrum_collatz.png")
    plt.close()

# =========================
# PLOT 3: loglog_regression.png
# =========================
def plot_loglog_regression():
    log_t = np.log10(t_values)
    log_E = np.log10(E_squared)

    slope, intercept = np.polyfit(log_t, log_E, 1)
    regression_line = np.poly1d((slope, intercept))(log_t)

    plt.figure(figsize=(8, 5))
    plt.plot(log_t, log_E, 'o', label="Data")
    plt.plot(log_t, regression_line, 'r--', label=f"Fit: slope = {slope:.2f}")
    plt.title("Log-Log Regression of Spectral Error")
    plt.xlabel(r"$\log_{10}(t)$")
    plt.ylabel(r"$\log_{10}(|E|^2)$")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("loglog_regression.png", dpi=300)
    plt.close()

# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":
    print("Generating Collatz Spectral Visualizations...")
    plot_mean_square_error()
    plot_raw_error_vs_t()
    plot_loglog_regression()
    print("✅ All plots saved successfully.")