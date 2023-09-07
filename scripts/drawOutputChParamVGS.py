import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_nmos_out_param_VGS.res'

res = np.loadtxt(filename,skiprows=1)

print(res.shape)

for curve in range(10):
    plt.plot(res[curve*331:(curve+1)*331,0],res[curve*331:(curve+1)*331,1]*1e6,label="VGS = "+'%.2f'%((curve+1)*0.33)+ " V")
plt.grid(b=True)
plt.legend(loc='upper right', frameon=False)
plt.xlim(0,5)
plt.xlabel("VDS [V]")
plt.ylabel("ID [uA]")
plt.title("Output characteristic W=1u L=500nm")

plt.show()
