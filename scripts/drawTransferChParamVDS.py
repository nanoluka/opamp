import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_nmos_transfer_param_VDS.res'

res = np.loadtxt(filename,skiprows=1)

print(res.shape)

for curve in range(10):
    plt.plot(res[curve*151:(curve+1)*151,0],res[curve*151:(curve+1)*151,1]*1e6,label="VDS = "+'%.2f'%((curve+1)*0.1)+ " V")
plt.grid(b=True)
plt.legend(loc='upper right', frameon=False)
plt.xlim(0,2.5)
plt.xlabel("VGS [V]")
plt.ylabel("ID [uA]")
plt.title("Transfer characteristic W=1um L=500nm")

plt.show()
