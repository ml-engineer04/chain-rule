import numpy as np
import sympy as sp

# ============================================================
# y = (2x-3)^2 -> g(x) = u = 2x-3 -> x=4 -> g(4) = 5 -> f(5) = 5^2 = 25
# y = (2x-3)^2 -> g(x) = u = 2x-3 -> x=0 -> g(0) = -3 -> f(-3) = (-3)^2 = 9
# y = (2x-3)^2 -> g(x) = u = 2x-3 -> x=1 -> g(1) = -1 -> f(-1) = (-1)^2 = 1
# ============================================================


# ============================================================
# Chain rule formula -> Zanjir qoidasi -> dy/dx = dy/du * du/dx
# ============================================================


# def g(x):
#     return 3 * x + 1


# def f(u):
#     return u**2


# def y(x):
#     return f(g(x))


# h = 0.0001
# x0 = 2

# numeric_dydx = (y(x0 + h) - y(x0)) / h

# chain_rule_dydx = 2 * g(x0) * 3

# print(f"Numeric: {numeric_dydx:.3f}")
# print(f"Chain rule: {chain_rule_dydx:.3f}")


# ============================================================
# sympy
# ============================================================

# x = sp.symbols("x")
# y = (3 * x + 1) ** 2

# dydx = sp.diff(y, x)
# print(f"dy/dx = {dydx}")
# print(f"x=2: -> {dydx.subs(x, 2)}")

# ============================================================
# task 2 with sympy
# ============================================================

# x = sp.symbols("x")
# y = (4 * x - 1) ** 2

# dydx = sp.diff(y, x)
# print(f"dy/dx = {dydx}")
# print(f"x=0: -> {dydx.subs(x, 0)}")
# print(f"x=1: -> {dydx.subs(x, 1)}")
# print(f"x=2: -> {dydx.subs(x, 2)}")


# ============================================================
# numeric
# ============================================================


# def g(x):
#     return 4 * x - 1


# def f(u):
#     return u**2


# def y(x):
#     return f(g(x))


# h = 0.0001
# x0 = 2
# numeric_dx = (y(x0 + h) - y(x0)) / h


# print(f"Numeric: x0 -> {x0}:  {numeric_dx:.3f}")

# Numeric: x0 -> 0:  -7.998
# Numeric: x0 -> 1:  24.002
# Numeric: x0 -> 2:  56.002


# ============================================================
# task 3 numeric
# ============================================================


# def g(x):
#     return x**2 + 3 * x


# def f(u):
#     return u**2


# def y(x):
#     return f(g(x))


# h = 0.0001
# x0 = 1
# numeric_dx = (y(x0 + h) - y(x0)) / h


# print(f"Numeric: x0 -> {x0}:  {numeric_dx:.3f}")


# ============================================================
# task 3 with sympy
# ============================================================

# x = sp.symbols("x")
# y = (x**2 + 3 * x) ** 2

# dydx = sp.diff(y, x)

# print(f"dy/dx = {dydx}")
# print(f"SymPy: -> x=1: -> {dydx.subs(x, 1)}")

# ============================================================
# task 3 with chain rule
# ============================================================

# chain_rule_dydx = 2 * g(x0) * (2 * x0 + 3)

# print(f"Chain rule: {chain_rule_dydx:.3f}")


# ============================================================
# how to read chain rule in neural network
# ============================================================

# x, w1, b1, target = 2, 0.5, 1, 10

# h = w1 * x + b1  # qatlam
# a = h**2  # aktivatsa
# loss = (a - target) ** 2  # xatolik

# # chain rule
# dLoss_da = 2 * (a - target)
# da_dh = 2 * h
# dh_dwl = x
# dLoss_dwl = dLoss_da * da_dh * dh_dwl

# print(f"dLoss_dwl -> {dLoss_dwl}")


# ============================================================
# task 4 -> b1 derivative
# ============================================================

# x, w1, b1, target = 2, 0.5, 1, 10

# h = w1 * x + b1  # qatlam
# a = h**2  # aktivatsa
# loss = (a - target) ** 2  # xatolik

# # chain rule
# dLoss_da = 2 * (a - target)
# da_dh = 2 * h
# dh_db1 = 1
# dLoss_dwl = dLoss_da * da_dh * dh_db1

# print(f"dLoss_dwl -> {dLoss_dwl}")
