import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("xy_data.csv")
    print("Data Loaded Successfully\n")
except FileNotFoundError:
    raise FileNotFoundError("Error: xy_data.csv not found. Place it in the same folder as this script.")

print(df.head())

if "t" in df.columns:
    t_vals = df["t"].values
else:
    t_vals = np.linspace(6, 60, len(df))  

x_obs = df["x"].values
y_obs = df["y"].values

def parametric_curve(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

def loss(params, t_vals, x_obs, y_obs):
    theta, M, X = params
    x_pred, y_pred = parametric_curve(t_vals, theta, M, X)
    return np.sum(np.abs(x_obs - x_pred) + np.abs(y_obs - y_pred))

initial_guess = [np.radians(25), 0.0, 10.0]
bounds = [
    (np.radians(0), np.radians(50)),
    (-0.05, 0.05),
    (0, 100)
]

result = minimize(loss, initial_guess, args=(t_vals, x_obs, y_obs), bounds=bounds, method="L-BFGS-B")

theta_opt, M_opt, X_opt = result.x

print("\n==================== RESULTS ====================")
print(f"Theta (radians): {theta_opt:.6f}")
print(f"Theta (degrees): {np.degrees(theta_opt):.6f}")
print(f"M: {M_opt:.6f}")
print(f"X: {X_opt:.6f}")
print("=================================================\n")

x_fit, y_fit = parametric_curve(t_vals, theta_opt, M_opt, X_opt)

plt.figure(figsize=(8, 6))
plt.scatter(x_obs, y_obs, color="blue", label="Observed Data", alpha=0.6)
plt.plot(x_fit, y_fit, color="red", linewidth=2, label="Fitted Curve")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Curve Fitting")
plt.grid(True)
plt.show()

submission_str = (
    f"\\left(t*\\cos({theta_opt:.4f})"
    f"-e^{{{M_opt:.4f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\sin({theta_opt:.4f})"
    f"+{X_opt:.4f},"
    f"42+t*\\sin({theta_opt:.4f})"
    f"+e^{{{M_opt:.4f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\cos({theta_opt:.4f})\\right)"
)

print(submission_str)
