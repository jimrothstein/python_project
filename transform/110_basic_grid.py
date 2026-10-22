"""Basic graph with x,y axes labeled using matplotlib."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Create sample data
x = np.linspace(0, 10, 100)
y = x * 0.15  # Simple linear replacement for sin(x)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Data generated but not plotted (line removed per user request)
# x and y are computed but intentionally not displayed

# Draw rectangle perimeter in blue with vertices at (0,0), (0,0.5), (1,0.5), (1,0)
rect = Rectangle((0, 0), 1, 0.5, edgecolor='blue', facecolor='none', linewidth=2)
ax.add_patch(rect)

# Label the axes
ax.set_xlabel('X axis', fontsize=12)
ax.set_ylabel('Y axis', fontsize=12)

# Add title
ax.set_title('Basic Grid Graph', fontsize=14)

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legend intentionally left empty since no plotted artists
# ax.legend()  # Removed: no artists to legendize

# Set axis limits with some margin
ax.set_xlim(-5, 5)
ax.set_ylim(-1.5, 1.5)

# Draw darker axis lines at x=0 (y-axis) and y=0 (x-axis)
ax.axvline(0, color='darkblue', linewidth=1.5)  # vertical line at x=0
ax.axhline(0, color='darkblue', linewidth=1.5)  # horizontal line at y=0

# Ensure equal aspect ratio is not forced so grid looks right
ax.set_aspect('auto')

# Save the figure
plt.tight_layout()
plt.savefig('basic_grid.png', dpi=150)
plt.show()