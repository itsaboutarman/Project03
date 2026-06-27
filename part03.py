import numpy as np
from scipy.integrate import trapezoid, simpson, quad
import matplotlib.pyplot as plt

# 1. Define the target mathematical function: f(x) = e^(x^2)
def f(x):
    return np.exp(x**2)

# Define integration limits [a, b]
a, b = 0, 1

# Generate an evenly spaced grid of N points for Simpson and Trapezoid
N = 1001  # Odd number of points ensures an even number of subintervals for Simpson
x_grid = np.linspace(a, b, N)
y_grid = f(x_grid)


# Part A: Trapezoidal and Simpson's Rule

trap_result = trapezoid(y_grid, x_grid)
simp_result = simpson(y_grid, x=x_grid)


# Part B: Gaussian Quadrature (High Precision Reference)

# scipy.integrate.quad uses the technique from the Fortran QUADPACK library (Gaussian Quadrature)
gauss_result, estimated_error = quad(f, a, b)


# Print Comparative Results

print("=== Numerical Integration Results for f(x) = e^(x^2) over [0, 1] ===")
print(f"1. Trapezoidal Rule  : {trap_result:.10f}")
print(f"2. Simpson's Rule    : {simp_result:.10f}")
print(f"3. Gaussian Quad     : {gauss_result:.10f}  (Absolute Error Margin: {estimated_error:.2e})")

# Calculate deviations relative to Gaussian Quadrature
print("\n=== Error Analysis (Compared to Gaussian Quadrature) ===")
print(f"Trapezoid Absolute Error : {abs(gauss_result - trap_result):.2e}")
print(f"Simpson Absolute Error   : {abs(gauss_result - simp_result):.2e}")


# Bonus Visual for Report: Shaded Area Under Curve

plt.figure(figsize=(7, 4.5), dpi=120)
plt.plot(x_grid, y_grid, 'r-', linewidth=2, label=r'$f(x) = e^{x^2}$')
plt.fill_between(x_grid, y_grid, color='red', alpha=0.15, label='Integrated Area')
plt.title(r'Definite Integral of $f(x) = e^{x^2}$ over $[0, 1]$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='upper left')
plt.grid(True, linestyle=':')
plt.savefig('part3_integral_area.png', dpi=300)
plt.close()