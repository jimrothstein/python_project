import numpy as np
import matplotlib.pyplot as plt

# Linear equation: y = 3*x + 2
# x from -1 to 1 in steps of 0.01

x = np.arange(-1, 1.01, 0.01)
y = 3 * x + 2
u = np.tanh(x)
v = np.tanh(y)

# Display as simple table with 4 columns
print(f"{'x':>6}  {'y':>6}  {'u':>6}  {'v':>6}")
print("-" * 29)
for xi, yi, ui, vi in zip(x, y, u, v):
    print(f"{xi:6.1f}  {yi:6.1f}  {ui:6.3f}  {vi:6.3f}")

# Plot and save
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = 3x + 2')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlim(-2, 2)
plt.ylim(-10, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 3x + 2')
plt.scatter(u, v, color='red', alpha=0.5, s=10, label='(u,v) = (tanh(x), tanh(y))')
plt.legend()
plt.savefig('410_simple_transform_plot.png', dpi=100)
plt.close()
print("\nPlot saved to 410_simple_transform_plot.png")