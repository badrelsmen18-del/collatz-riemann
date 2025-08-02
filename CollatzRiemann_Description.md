# Collatz–Riemann Visualizations

This repository contains the Python code used to generate key figures for the paper:

**"Collatz Spectral Dynamics and the Mean-Square Vanishing of the Zeta Tail"**  
Author: Badr Elsayed Aboelyazeed Elsaman

---

##  Contents

The script `collatz_visualizations.py` reproduces the following figures:

1. **Mean-Square Error Decay** of the tail term \( E(1/2 + it) \)
2. **Log-Log Regression** of the decay curve showing power-law behavior with slope ≈ -0.83
3. (Optional) Combined or extended plots from the research

These visualizations support the analytical result that the tail error term vanishes in mean-square on the critical line \( \Re(s) = \frac{1}{2} \), providing numerical evidence for spectral equivalence between the Collatz and Riemann zeta functions.

---

## Requirements

- Python 3.x
- matplotlib
- numpy

To install dependencies:
```bash
pip install matplotlib numpy
