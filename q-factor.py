from sympy import *

R, L, C, omega = symbols("R L C omega", real=True)

U_2 = 1/(I + omega * C)

U_1 = R + 1/(I * omega * C)  + I * omega * L

ratio = expand(U_2 / U_1)

im_ratio = ratio.as_real_imag()[1]
re_ratio = ratio.as_real_imag()[0]


omega0 = solve(im_ratio-re_ratio, omega)[1]
