import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Example: Non-linear relationship (e.g., y = 3x^2 + 2x + noise)
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 3 * X.squeeze()**2 + 2 * X.squeeze() + np.random.randn(100) * 10

# Linear Regression on original feature
model_linear = LinearRegression()
model_linear.fit(X, y)
y_pred_linear = model_linear.predict(X)
r2_linear = r2_score(y, y_pred_linear)

# Polynomial Features (degree=2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
model_poly = LinearRegression()
model_poly.fit(X_poly, y)
y_pred_poly = model_poly.predict(X_poly)
#compare actutal vs predicted values
r2_poly = r2_score(y, y_pred_poly)

print(f"R^2 score (Linear): {r2_linear:.4f}")
print(f"R^2 score (Polynomial degree=2): {r2_poly:.4f}")

if r2_poly > r2_linear:
	print("Polynomial features improved the model.")
else:
	print("Polynomial features did not improve the model.")