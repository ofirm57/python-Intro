import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *

# הגדרת משתנים
#
W = np.linspace(0, 10 ** 5, 1000)
C = 10 ** -6
L = 10 * 10 ** -3
V0 = 1
R1 = 0.5 * 10 ** 3
R2 = 10 ** 3
R3 = 3 * 10 ** 3

# 3W = symbols('W')
# var('w')

# eq1 = Eq(  V0 / ((R2 / (C ** 2 * R2 ** 2 * W ** 2 + 1)
#            + (L ** 2 * R3 * W ** 2) / (
#         L ** 2 * W ** 2 + R3 ** 2) + R1) ** 2 + (
#                (L * R3 ** 2 * W) / (L ** 2 * W ** 2 + R3 ** 2)
#                - (C * R2 ** 2 * W) /
#                (C ** 2 * R2 ** 2 * W ** 2 + 1)) ** 2) ** 0.5 ,1)
#
# sol = solve(eq1)
# print(sol)

# הערך של I בערך מוחלט
I = V0 / ((R2 / (C ** 2 * R2 ** 2 * W ** 2 + 1)
           + (L ** 2 * R3 * W ** 2) / (
        L ** 2 * W ** 2 + R3 ** 2) + R1) ** 2 + (
               (L * R3 ** 2 * W) / (L ** 2 * W ** 2 + R3 ** 2)
               - (C * R2 ** 2 * W) /
               (C ** 2 * R2 ** 2 * W ** 2 + 1)) ** 2) ** 0.5


plt.xlabel('W [rad/sec]')
plt.ylabel('| I |')
plt.plot(W, I, 'b')
plt.axhline(y=1 * 10 ** -3, color='r', linestyle=':')

plt.grid()
plt.show()
