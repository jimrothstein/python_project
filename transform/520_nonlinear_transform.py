"""Nonlinear transform, step 1: draw a unit square."""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Step 1: the unit square, corners (0,0), (1,0), (1,1), (0,1).
square = np.array([[0, 0],
                   [1, 0],
                   [1, 1],
                   [0, 1],
                   [0, 0]], dtype=float)

print("Step 1: unit square")
print("corners (closed loop):")
print(square)

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(square[:, 0], square[:, 1], "o-", lw=2, color="tab:blue")

for x, y in square[:-1]:
    ax.annotate(f"({x:g}, {y:g})", (x, y), textcoords="offset points",
                xytext=(6, 6), fontsize=9)

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.set_title("Step 1: unit square")

fig.savefig("51O_nonlinear_transform.png", dpi=150, bbox_inches="tight")
print("saved 51O_nonlinear_transform.png")

# ------------------------------------------------------------------
# Step 2: nonlinear transform  f(x,y) = (x^2 - y^2, 2*x*y)
# (complex squaring: (x+iy)^2)
# Sample the perimeter so curved edges are visible.
print("\nStep 2: nonlinear transform f(x,y) = (x^2 - y^2, 2*x*y)")

def transform(pts):
    x = pts[:, 0]
    y = pts[:, 1]
    return np.column_stack([x**2 - y**2, 2 * x * y])

# sample each edge of the unit square
n = 200
edges = []
for (a, b) in [((0, 0), (1, 0)), ((1, 0), (1, 1)),
               ((1, 1), (0, 1)), ((0, 1), (0, 0))]:
    t = np.linspace(0, 1, n)
    pts = np.array(a) + t[:, None] * (np.array(b) - np.array(a))
    edges.append(pts)
perim = np.vstack(edges)
trans = transform(perim)

print("original perimeter shape:", perim.shape)
print("transformed perimeter shape:", trans.shape)
print("original corners -> transformed:")
for c in square[:-1]:
    print(f"  {tuple(c)} -> {tuple(transform(c[None, :])[0])}")

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(perim[:, 0], perim[:, 1], "b-", lw=1.5)
ax1.set_title("Original square")
ax1.set_aspect("equal"); ax1.grid(True, alpha=0.3)
ax1.set_xlim(-0.2, 1.2); ax1.set_ylim(-0.2, 1.2)

ax2.plot(trans[:, 0], trans[:, 1], "r-", lw=1.5)
ax2.set_title("After f(x,y)=(x^2-y^2, 2xy)")
ax2.set_aspect("equal"); ax2.grid(True, alpha=0.3)

fig2.savefig("51O_nonlinear_transform_step2.png", dpi=150, bbox_inches="tight")
print("saved 51O_nonlinear_transform_step2.png")

# ------------------------------------------------------------------
# Step 3: 5 random points inside the square; transform and plot them
print("\nStep 3: 5 random points inside the square")
rng = np.random.default_rng(42)
pts = rng.random((5, 2))  # x,y in [0,1)
pts_t = transform(pts)

print("original points:")
print(pts)
print("transformed points:")
print(pts_t)

fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(perim[:, 0], perim[:, 1], "b-", lw=1, alpha=0.5)
ax1.scatter(pts[:, 0], pts[:, 1], c="black", s=60, zorder=5)
for i, (x, y) in enumerate(pts):
    ax1.annotate(f"P{i}", (x, y), textcoords="offset points", xytext=(6, 6), fontsize=9)
ax1.set_title("Original: square + 5 random points")
ax1.set_aspect("equal"); ax1.grid(True, alpha=0.3)
ax1.set_xlim(-0.2, 1.2); ax1.set_ylim(-0.2, 1.2)

ax2.plot(trans[:, 0], trans[:, 1], "r-", lw=1, alpha=0.5)
ax2.scatter(pts_t[:, 0], pts_t[:, 1], c="black", s=60, zorder=5)
for i, (x, y) in enumerate(pts_t):
    ax2.annotate(f"P{i}", (x, y), textcoords="offset points", xytext=(6, 6), fontsize=9)
ax2.set_title("Transformed: curve + 5 points")
ax2.set_aspect("equal"); ax2.grid(True, alpha=0.3)

fig3.savefig("520_nonlinear_transform_step3.png", dpi=150, bbox_inches="tight")
print("saved 520_nonlinear_transform_step3.png")

# ------------------------------------------------------------------
# Step 4: horizontal line segment y = 0.2 inside the square; transform it
print("\nStep 4: line segment y = 0.2")
xs = np.linspace(0.0, 1.0, 300)
line = np.column_stack([xs, np.full_like(xs, 0.2)])
line_t = transform(line)

fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(perim[:, 0], perim[:, 1], "b-", lw=1, alpha=0.4)
ax1.plot(line[:, 0], line[:, 1], "k-", lw=2, label="y=0.2")
ax1.set_title("Original: y = 0.2 segment")
ax1.set_aspect("equal"); ax1.grid(True, alpha=0.3)
ax1.set_xlim(-0.2, 1.2); ax1.set_ylim(-0.2, 1.2); ax1.legend()

ax2.plot(trans[:, 0], trans[:, 1], "r-", lw=1, alpha=0.4)
ax2.plot(line_t[:, 0], line_t[:, 1], "k-", lw=2, label="transformed")
ax2.set_title("Transformed y = 0.2")
ax2.set_aspect("equal"); ax2.grid(True, alpha=0.3); ax2.legend()

fig4.savefig("520_nonlinear_transform_step4.png", dpi=150, bbox_inches="tight")
print("saved 520_nonlinear_transform_step4.png")
