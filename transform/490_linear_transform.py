import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)

print("=== Linear Transformations with NumPy ===\n")

# 1. Basic definition: T(x) = A @ x
print("1. Linear Transform T(x) = A @ x")
A = np.array([[2, 0],
              [0, 3]])
x = np.array([1, 2])
Tx = A @ x
print(f"   A = \n{A}")
print(f"   x = {x}")
print(f"   T(x) = A @ x = {Tx}")
print()

# 2. Properties: T(u+v) = T(u) + T(v), T(c*u) = c*T(u)
print("2. Verifying linearity properties")
u = np.array([1, 0])
v = np.array([0, 1])
c = 3
print(f"   T(u + v) = {A @ (u + v)}")
print(f"   T(u) + T(v) = {A @ u + A @ v}")
print(f"   T(c*u) = {A @ (c * u)}")
print(f"   c*T(u) = {c * (A @ u)}")
print()

# 3. Common transform matrices
print("3. Common 2D Linear Transforms")

# Identity
I = np.eye(2)
print(f"   Identity:\n{I}")

# Scaling
S = np.array([[2, 0], [0, 0.5]])
print(f"   Scale x by 2, y by 0.5:\n{S}")

# Rotation by 45 degrees
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
print(f"   Rotate 45°:\n{R}")

# Shear
H = np.array([[1, 1.5], [0, 1]])
print(f"   Shear x by 1.5:\n{H}")

# Reflection across x-axis
Ref = np.array([[1, 0], [0, -1]])
print(f"   Reflect across x-axis:\n{Ref}")
print()

# 4. Composition of transforms
print("4. Composition: Rotation then Scaling")
A_composed = S @ R
print(f"   S @ R =\n{A_composed}")
test_vec = np.array([1, 1])
print(f"   Apply to [1, 1]: {A_composed @ test_vec}")
print()

# 5. Apply to a set of vectors (shape of a square)
print("5. Transform a unit square")
square = np.array([[0, 0],
                   [1, 0],
                   [1, 1],
                   [0, 1],
                   [0, 0]]).T  # shape (2, 5)

transformed = S @ R @ square
print(f"   Original vertices:\n{square.T}")
print(f"   Transformed vertices:\n{transformed.T}")
print()

# 6. Inverse transform (if invertible)
print("6. Inverse Transform")
if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    print(f"   A_inv = \n{A_inv}")
    print(f"   A @ A_inv = \n{A @ A_inv}")
    print(f"   Recover x: {A_inv @ Tx}")
else:
    print("   A is singular, no inverse")
print()

# 7. Linear transform in ML context: StandardScaler
print("7. ML Context: StandardScaler (linear transform on features)")
from sklearn.preprocessing import StandardScaler
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
print(f"   Original X:\n{X}")
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)
print(f"   Scaled X (zero mean, unit variance):\n{X_scaled}")
print(f"   mean_ = {scaler.mean_}")
print(f"   scale_ = {scaler.scale_}")
print()

# 8. Eigendecomposition
print("8. Eigendecomposition of transform matrix")
eigvals, eigvecs = np.linalg.eig(R)
print(f"   Rotation eigenvalues: {eigvals}")
print(f"   Rotation eigenvectors:\n{eigvecs}")
print()

# 9. SVD
print("9. Singular Value Decomposition (SVD)")
U, s, Vt = np.linalg.svd(A_composed)
print(f"   U:\n{U}")
print(f"   s: {s}")
print(f"   V^T:\n{Vt}")
print(f"   Reconstructed: \n{U @ np.diag(s) @ Vt}")
print()

print("=== Done ===")