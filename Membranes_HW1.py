import numpy as np
import matplotlib.pyplot as plt

# ---- Data ----

# Membrane 1

C_f1 = [0.01, 0.015, 0.014, 0.05, 0.06, 0.065, 0.08, 0.1]
C_p1 = [0.01, 0.0144, 0.0102, 0.0204, 0.00923, 0.00102, 0.000741, 0.000545]
mw_1 = [10, 25, 35, 45, 57, 80, 85, 90] 

# Membrane 2

C_f2 = [0.012, 0.01, 0.016, 0.03, 0.045, 0.068, 0.09, 0.11, 0.12, 0.014]
C_p2 = [0.012, 0.00889, 0.011, 0.015, 0.01796, 0.0191, 0.02, 0.0174, 0.0136, 0.00103]
mw_2 = [10, 25, 40, 55, 65, 80, 90, 105, 120, 140]

# ---- Calculate Reection ----

def calculate_rejection(C_f, C_p):
    R = []
    for i in range(len(C_f)):
        R.append(1 - (C_p[i] / C_f[i]))
    return R

R1 = calculate_rejection(C_f1, C_p1)
R2 = calculate_rejection(C_f2, C_p2)

# ---- Find cutoff value ----
def find_cutoff(mw, R):
     
    for i in range(len(mw)):
        if R[i] == 0.9:
            return mw[i]
        elif R[i] > 0.9 and R[i-1] < 0.9:
            # Linear interpolation to find the cutoff value
            return mw[i-1] + (0.9 - R[i-1]) * (mw[i] - mw[i-1]) / (R[i] - R[i-1])
            
cutoff_1 = find_cutoff(mw_1, R1)
cutoff_2 = find_cutoff(mw_2, R2)

# ---- Plot Rejection vs Molecular Weight ----

plt.figure(figsize=(10, 6))
plt.plot(mw_1, R1, 'o-', label='Membrane 1')
plt.plot(mw_2, R2, 's-', label='Membrane 2')
plt.hlines(y=0.9, xmin=0, xmax=max(cutoff_1, cutoff_2), color='red', linestyle='--', label='90% Rejection')
plt.vlines(x=cutoff_1, ymin=0, ymax=0.9, color='blue', linestyle='--', label=f'Membrane 1 Cutoff: {cutoff_1:.2f} 'r'$\frac{g}{mol}$')
plt.vlines(x=cutoff_2, ymin=0, ymax=0.9, color='green', linestyle='--', label=f'Membrane 2 Cutoff: {cutoff_2:.2f} 'r'$\frac{g}{mol}$')
plt.xlabel(r'Molecular Weight ($\frac{g}{mol}$)')
plt.ylabel('Rejection (R)')
plt.title('Rejection vs Molecular Weight for Two Membranes')
plt.legend()
plt.grid()
plt.show()