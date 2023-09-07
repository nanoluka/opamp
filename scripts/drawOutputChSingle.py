import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_nmos_out_single.res'

res = np.loadtxt(filename,skiprows=1)

print(res.shape)

plt.plot(res[:,0],res[:,1]*1000)
plt.grid(b=True)
plt.xlabel("VDS [V]")
plt.ylabel("ID [mA]")
plt.title("Output characteristic")
plt.show()
