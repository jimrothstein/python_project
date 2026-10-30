#!/usr/bin/env python3
# REF:  sci-learn
import numpy as np

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
print(X)
print(y)


