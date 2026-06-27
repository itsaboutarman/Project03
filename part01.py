import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1, 3, 5, 8, 5, 2])

# Part A: Lagrange Interpolation

poly_lagrange = lagrange(x, y)

print("=== Lagrange Polynomial Exact Formula ===")
print(np.poly1d(poly_lagrange))


# Part B: Cubic Spline Interpolation

cs = CubicSpline(x, y)

print("\n=== Cubic Spline Exact Formulas (Per Interval) ===")
# S(x) = a*(x - x_i)^3 + b*(x - x_i)^2 + c*(x - x_i) + d
for i in range(len(x) - 1):
    a, b, c, d = cs.c[:, i]
    xi = x[i]
    print(f"Interval [{x[i]}, {x[i+1]}]:")
    print(f"  S_{i+1}(x) = ({a:+.4f})*(x - {xi})^3 + ({b:+.4f})*(x - {xi})^2 + ({c:+.4f})*(x - {xi}) + ({d:+.4f})")


# Part C: Plotting the Interpolations
x_dense = np.linspace(1, 6, 200)

plt.figure(figsize=(9, 5), dpi=120)
plt.scatter(x, y, color='red', s=50, zorder=5, label='Data Points')
plt.plot(x_dense, poly_lagrange(x_dense), 'b--', label='Lagrange Interpolation')
plt.plot(x_dense, cs(x_dense), 'g-', label='Cubic Spline')

plt.title('Lagrange vs Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle=':')

# Save the high-resolution figure for the project report
plt.savefig('part1_interpolation.png', dpi=300)
plt.show()