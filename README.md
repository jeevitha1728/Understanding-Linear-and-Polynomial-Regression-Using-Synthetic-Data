# Understanding-Linear-and-Polynomial-Regression-Using-Synthetic-Data

Objective
The goal of this assignment is to help you visually and conceptually understand
how linear regression behaves under different levels of model complexity, and
how overfitting emerges. By the end of this assignment, you should be able to
explain why a model performs well or poorly—not just report numbers.

Dataset Explanation:
The target variable *rent*
Only number_of_houses was used for modeling to allow clear 2D visualization.

The dataset was split into:

75% training

25% testing

Models Built
1. Simple Linear Regression
y=mx+c

This model can only learn straight-line relationships.

2. Polynomial Regression
y = a + bx + cx²

Polynomial regression of degree 2 was implemented

Why Squared Error Is Used
Squaring makes large mistakes much more than small ones.
Prevents positive and negative errors from canceling each other.

Data + Model Predictions:
Linear Regression
Produces a straight line
Fails to follow the curved structure
Clearly underfits

Polynomial Regression (Degree 2):
Produces a smooth curve
Closely follows the data trend
Captures the true underlying relationship

As a result:
Test error decreases initially
Then increases after a certain degree

R² Interpretation:
Linear regression R² is lower due to underfitting
Polynomial regression R² is higher because it captures curvature

Final Conclusion:
This assignment demonstrates that:

Linear models underfit non-linear data
Polynomial models can capture curvature
Excessive complexity leads to overfitting


r2_score :
 the linear value  0.987
 the poly value  0.997
