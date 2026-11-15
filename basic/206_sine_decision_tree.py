##### !/usr/bin/env python3
# Sine regression with a shallow decision tree (max_depth=2), N points (N=80 below).
#
# HOW TO RUN (a venv, NOT system python -- pip is blocked there by PEP 668).
# Two venvs both work (they need sklearn, matplotlib, pandas, tabulate):
#   ~/code/python_project/.venv/bin/python ~/code/python_project/206_sine_decision_tree.py
#   ~/.venvs/ml/bin/python                 ~/code/python_project/206_sine_decision_tree.py
#
# OUTPUTS (overwritten each run):
#   /tmp/opencode/tree_blue_points.png   graph: data dots + blue prediction line
#   /tmp/opencode/tree_plot_sine.png     the tree itself (splits + leaf rules)
#   /tmp/opencode/table80.txt            ALL N rows: row, x, y_pred, y_true, err
# REF: https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

# 80 points, N/5 will be noisy
N=80
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(N, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(len(y[::5])))  # every 5 is noisy points

d2 = DecisionTreeRegressor(max_depth=2).fit(X, y)
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_pred = d2.predict(X_test)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, s=10, label="data (x, y)")
plt.plot(X_test, y_pred, color="tab:blue", linewidth=2, label="prediction (x, y_pred)")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"DecisionTreeRegressor(max_depth=2), n={N}")
plt.legend()
plt.tight_layout()
plt.savefig("/tmp/opencode/tree_blue_points.png", dpi=100)

# draw the tree itself (splits + leaf rules) -- like tree.plot_tree(clf) for iris
fig, ax = plt.subplots(figsize=(10, 5))
tree.plot_tree(d2, ax=ax)
fig.tight_layout()
fig.savefig("/tmp/opencode/tree_plot_sine.png", dpi=100)
plt.close(fig)

# save datapoints
df = pd.DataFrame({"x": X.ravel(), "y_pred": d2.predict(X), "y_true": y})
df["err"] = df.y_true - df.y_pred
tbl = df.round(4).to_markdown(index=True, headers=["row", "x", "y_pred", "y_true", "err"])
with open("/tmp/opencode/table80.txt", "w") as f:
    f.write(tbl + "\n")

assert len(df) == N
print(f"saved: {N} rows -> /tmp/opencode/table80.txt, png -> /tmp/opencode/tree_blue_points.png, tree -> /tmp/opencode/tree_plot_sine.png")
