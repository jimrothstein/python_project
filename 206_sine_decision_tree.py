#!/usr/bin/env python3
# Sine regression with a shallow decision tree (max_depth=2), 1000 points.
#
# HOW TO RUN (uses the ~/.venvs/ml venv -- NOT system python):
#   ~/.venvs/ml/bin/python ~/code/python_project/206_sine_decision_tree.py
#   (venv has sklearn, matplotlib, pandas installed; pip is blocked on
#    system python by PEP 668)
#
# OUTPUTS (overwritten each run):
#   /tmp/opencode/tree_blue_points.png   graph: data dots + blue prediction line
#   /tmp/opencode/table80.txt            ALL 1000 rows: row, x, y_pred, y_true, err
# REF: https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(1000, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(len(y[::5])))  # 200 noisy points

d2 = DecisionTreeRegressor(max_depth=2).fit(X, y)
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_pred = d2.predict(X_test)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, s=10, label="data (x, y)")
plt.plot(X_test, y_pred, color="tab:blue", linewidth=2, label="prediction (x, y_pred)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("DecisionTreeRegressor(max_depth=2), n=1000")
plt.legend()
plt.tight_layout()
plt.savefig("/tmp/opencode/tree_blue_points.png", dpi=100)

df = pd.DataFrame({"x": X.ravel(), "y_pred": d2.predict(X), "y_true": y})
df["err"] = df.y_true - df.y_pred
tbl = df.round(4).to_markdown(index=True, headers=["row", "x", "y_pred", "y_true", "err"])
with open("/tmp/opencode/table80.txt", "w") as f:
    f.write(tbl + "\n")

assert len(df) == 1000
print("saved: 1000 rows -> /tmp/opencode/table80.txt, png -> /tmp/opencode/tree_blue_points.png")
