# Assignment for Research and Development / AI

---

## 🧩 Problem Statement

Find the values of unknown parameters in the given **parametric equation of a curve**:

\[
x = \left( t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t)\sin(\theta) + X \right)
\]

\[
y = \left( 42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t)\cos(\theta) \right)
\]

where the unknowns are:

\[
\theta, \; M, \; X
\]

with the following constraints:

\[
0^\circ < \theta < 50^\circ, \quad -0.05 < M < 0.05, \quad 0 < X < 100
\]
and the parameter range:
\[
6 < t < 60
\]

The dataset `xy_data.csv` contains points that lie on this curve.

---

## 🧮 Derived Parametric Equations (Final Result)

After optimization, the best-fit parametric form of the curve is:

\[
\left(
t*\cos(0.4908)
- e^{0.0214|t|} \cdot \sin(0.3t)\sin(0.4908)
+ 54.9001,
\;
42 + t*\sin(0.4908)
+ e^{0.0214|t|} \cdot \sin(0.3t)\cos(0.4908)
\right)
\]

This equation can be directly plotted in [Desmos](https://www.desmos.com/calculator).

---

## ⚙️ Explanation of Steps

### **1️⃣ Data Loading**
- The dataset `xy_data.csv` was loaded using `pandas`.  
- It contained the observed coordinates `(x, y)` for points on the unknown curve.  
- Since the dataset did not include `t`, evenly spaced `t` values were generated between 6 and 60.

### **2️⃣ Equation Definition**
The given equations were implemented in Python as:
```python
x = t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X
y = 42 + t*np.sin(theta) + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta)

3️⃣ Loss Function

To find the optimal parameters, an L1 loss function was used:

𝐿
=
∑
∣
𝑥
𝑜
𝑏
𝑠
−
𝑥
𝑝
𝑟
𝑒
𝑑
∣
+
∣
𝑦
𝑜
𝑏
𝑠
−
𝑦
𝑝
𝑟
𝑒
𝑑
∣
L=∑∣x
obs
	​

−x
pred
	​

∣+∣y
obs
	​

−y
pred
	​

∣

This measures the total absolute deviation between the predicted and observed points.

4️⃣ Optimization

The scipy.optimize.minimize() function was used with the L-BFGS-B method.

Parameter bounds were set based on the given constraints.

Initial guesses:

𝜃
0
=
25
∘
,
𝑀
0
=
0.0
,
𝑋
0
=
10
θ
0
	​

=25
∘
,M
0
	​

=0.0,X
0
	​

=10

The algorithm iteratively adjusted these parameters to minimize the L1 distance between the predicted and observed points.

5️⃣ Visualization

The fitted curve was plotted against the actual data using matplotlib.

Blue points: observed data from the CSV.

Red curve: model-predicted curve using optimized parameters.

The close overlap between the two shows a strong fit.

| Parameter   | Symbol | Value      |
| ----------- | ------ | ---------- |
| θ (radians) | θ      | 0.490754   |
| θ (degrees) | θ      | 28.118153° |
| M           | M      | 0.021387   |
| X           | X      | 54.900078  |

🧠 Interpretation

θ (theta) defines the angular orientation of the curve.

M controls the exponential scaling and oscillation amplitude (positive M adds upward curvature).

X shifts the entire curve along the x-axis.

Together, these parameters reproduce the observed shape with excellent accuracy.

## Final Submission Equation:

\left(t*\cos(0.4908)-e^{0.0214\left|t\right|}\cdot\sin(0.3t)\sin(0.4908)+54.9001,42+t*\sin(0.4908)+e^{0.0214\left|t\right|}\cdot\sin(0.3t)\cos(0.4908)\right)

## conclusion:

✅ Conclusion

By using numerical optimization and parametric modeling,
the unknown variables 
𝜃
,
𝑀
,
𝑋
θ,M,X were successfully determined such that
the generated curve closely matches the provided dataset.

This approach demonstrates:

Proper mathematical modeling of nonlinear parametric systems,

Application of optimization algorithms (scipy.optimize.minimize),

And effective curve-fitting validation through visualization.