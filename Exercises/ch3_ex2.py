# Bradley Orzolek
# Chapter 3: Packages for Data Manipulation
# Exercise 2
# 5/17/2021

import numpy as np

x = np.load("exercises/data/x.npy")
y = np.load("exercises/data/y.npy")
b = np.load("exercises/data/b.npy")

y_pred = b[0] + b[1]*x[:,1]

residuals_sq = (y_pred - y)**2
RMSE = np.sqrt(np.mean(residuals_sq))

print(f"RMSE = {RMSE: .2f}")
