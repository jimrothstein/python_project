Here's a complete summary of every function/class in `205_trees.py`:

---

## Imports

```python
import math
import random
```

**Purpose:** Standard library. `math` for log/trig/sqrt, `random` for bootstrap sampling and random feature selection.

---

## `gini_impurity(labels)`

```python
def gini_impurity(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((c / n) ** 2 for c in counts.values())
```

**Purpose:** Measures class impurity. 0 = all same class, higher = more mixed.

| `labels` | Gini |
|---|---|
| `["a","a","a"]` | 0.0 |
| `["a","a","b"]` | 0.444 |
| `["a","b"]` | 0.500 |

---

## `entropy(labels)`

```python
def entropy(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return -sum(
        (c / n) * math.log2(c / n) for c in counts.values() if c > 0
    )
```

**Purpose:** Same goal as Gini, different formula. Uses log base 2.

| `labels` | Entropy |
|---|---|
| `["a","a","a"]` | 0.000 |
| `["a","a","b"]` | 0.918 |
| `["a","b"]` | 1.000 |

Max for 2 classes = 1.0, for 4 classes = 2.0.

---

## `information_gain(parent, left, right, criterion)`

**Purpose:** How much a split reduces impurity. Higher = better split. Criterion picks Gini or Entropy.

| parent | left | right | IG(Gini) |
|---|---|---|---|
| `[a,a,b,b]` | `[a,a]` | `[b,b]` | 0.500 |
| `[a,a,b,b]` | `[a,a,b]` | `[b]` | 0.167 |

Returns 0 if either child is empty (split wasn't useful).

---

## `variance_reduction(parent, left, right)`

**Purpose:** Same idea as information gain, but for **regression targets**. Uses variance instead of class impurity.

| parent | left | right | VR |
|---|---|---|---|
| `[2,4,6,8]` | `[2,4]` | `[6,8]` | 5.0 - 1.0 = 4.0 |

---

## `_variance(values)` and `_mean(values)`

**Purpose:** Private helpers. `_variance` computes population variance, `_mean` computes average. Both handle empty list (return 0.0).

**Example `_variance([2,4,6])`:** mean=4, variance = `(4+0+4)/3` = 2.667

---

## `majority_vote(labels)`

```python
def majority_vote(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return max(counts, key=counts.get)
```

**Purpose:** Returns the most frequent label. Used for classification leaves.

**Example `["a","a","b"]`:** returns `"a"`.

---

## `class DecisionTree`

### `__init__`

```python
def __init__(self, max_depth=None, min_samples_split=2,
             min_samples_leaf=1, criterion="gini",
             max_features=None, task="classification"):
```

**Purpose:** Stores hyperparameters. `max_depth=None` means grow fully. `task` switches between classification/regression.

---

### `fit(X, y)`

```python
def fit(self, X, y):
    self.n_features = len(X[0])
    self.feature_importances_ = [0.0] * self.n_features
    self.n_samples = len(X)
    self.tree = self._build(X, y, depth=0)
    total = sum(self.feature_importances_)
    if total > 0:
        self.feature_importances_ = [
            fi / total for fi in self.feature_importances_
        ]
```

**Purpose:** Entry point. Records dimensions, builds the tree recursively, then normalizes feature importances.

---

### `predict(X)`

```python
def predict(self, X):
    return [self._predict_one(x, self.tree) for x in X]
```

**Purpose:** Runs each sample through the tree and returns a list of predictions.

---

### `_build(X, y, depth)` — the recursive tree builder

**Purpose:** Core algorithm. Returns either a leaf dict or a split node dict.

**Stopping conditions** (in order):
1. All labels same → leaf
2. `max_depth` reached → leaf
3. Too few samples (`< min_samples_split`) → leaf
4. No split improves impurity → leaf
5. Children too small (`< min_samples_leaf`) → leaf

**Otherwise:** Finds best split, accumulates feature importance, recurses on left and right.

**Return format:**
```python
# Leaf:
{"leaf": True, "value": <prediction>}

# Split node:
{"leaf": False, "feature": <idx>, "threshold": <float>,
 "left": <node>, "right": <node>}
```

---

### `_best_split(X, y)`

**Purpose:** Finds the best feature + threshold by trying all candidates.

- If `max_features=None` → try all features
- If `"sqrt"` → try `sqrt(n_features)` random features
- If `int` → try that many random features
- For each feature, sorts unique values, tries midpoints as thresholds
- Picks the one with highest gain

---

### `_split_data(X, y, feature, threshold)`

**Purpose:** Partitions data into left (≤ threshold) and right (> threshold).

---

### `_predict_one(x, node)`

**Purpose:** Walks a single sample through the tree recursively.

```python
if node["leaf"]:
    return node["value"]
if x[node["feature"]] <= node["threshold"]:
    return self._predict_one(x, node["left"])
return self._predict_one(x, node["right"])
```

---

### `print_tree(node, indent)`

**Purpose:** Pretty-prints the tree structure showing splits and leaf predictions.

**Example output:**
```
Feature 0 <= 1.5000?
  Yes:
    Predict: 0
  No:
    Feature 1 <= 0.3000?
      Yes:
        Predict: 1
      No:
        Predict: 2
```

---

## `class RandomForest`

### `__init__`

```python
def __init__(self, n_trees=100, max_depth=None,
             min_samples_split=2, max_features="sqrt",
             criterion="gini", task="classification"):
```

**Purpose:** Default `max_features="sqrt"` is the key difference from single trees.

---

### `fit(X, y)`

**Purpose:** Bootstrap sampling. For each tree, draw n samples **with replacement**, train a `DecisionTree` on that bootstrapped data. Stores all trees in `self.trees`.

---

### `predict(X)`

**Purpose:** Collects predictions from all trees. Classification → **majority vote**. Regression → **average**.

---

### `feature_importances()`

**Purpose:** Averages feature importances across all trees, normalizes to sum to 1.

---

## Utility functions

### `accuracy(y_true, y_pred)`

**Purpose:** `correct / total`. Returns float 0–1.

### `generate_classification_data(n_samples, seed)`

**Purpose:** Creates 2D synthetic data with 3 classes based on circles + lines + noise.

### `generate_regression_data(n_samples, seed)`

**Purpose:** Creates 1D synthetic data: `y = sin(x) * x + noise`.

### `train_test_split(X, y, test_ratio, seed)`

**Purpose:** Shuffles and splits into train/test. Default 80/20.

---

## Demo functions

| Function | What it shows |
|---|---|
| `demo_split_criteria()` | Gini vs Entropy values for various label distributions |
| `demo_information_gain()` | Which split wins with different feature candidates |
| `demo_decision_tree()` | Effect of `max_depth` on train/test accuracy |
| `demo_gini_vs_entropy()` | Gini and entropy produce nearly identical results |
| `demo_random_forest()` | More trees → better test accuracy, diminishing returns |
| `demo_feature_importance()` | Tree correctly identifies important vs noise features |
| `demo_regression_tree()` | Regression tree MSE at different depths; RF smoother |
| `demo_single_tree_vs_forest()` | Single trees have high variance, forests are stable |
| `print_summary()` | 7 key takeaways |

**Execution** (`if __name__ == "__main__"`): Runs all demos in sequence.
