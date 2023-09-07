import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_opamp_op.res'

res = np.loadtxt(filename)

print(res.shape)
print(np.transpose(res))
