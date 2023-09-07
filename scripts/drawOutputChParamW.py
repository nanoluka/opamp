import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_nmos_output_param_Width.res'

res = np.loadtxt(filename,skiprows=1)

print(res.shape)
cols = res.shape[1]

for curve in range(cols-1):
    plt.plot(res[:,0],res[:,curve+1]*1e3,label="W = "+str(curve+1)+" um")
plt.grid(b=True)
plt.legend(loc='upper right', frameon=False)
plt.xlim(0,5)
plt.xlabel("VDS [V]")
plt.ylabel("ID [mA]")
plt.title("Output characteristic @L=500nm")

plt.show()
