import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_nmos_unitygain_single.res'

res = np.loadtxt(filename,skiprows=1)

print(res.shape)

plt.semilogx(res[:,0],res[:,1])
p1 = [res[1,0],res[100,0]]
p2 = [res[1,1],res[100,1]]
plt.ylabel("ID/IG [dB]")
plt.xlabel("Frequency [Hz]")
plt.ylim([-50,250])
plt.grid("on")
pz1 = [res[1,0],res[107,0]]
pz2 = [res[1,1],0]
plt.plot(pz1,pz2,color='k',marker='o', linewidth=0.5, linestyle="--", label="fT = "+"%.2f" % (res[107,0]/1e9) + "GHz")
plt.legend(loc="lower left")
plt.show()
