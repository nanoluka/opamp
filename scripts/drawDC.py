import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_opamp_dc_diff.res'

res = np.loadtxt(filename,skiprows=1)

fig, ax = plt.subplots()
negInLim = np.where(res[:,3] < 3.13)[0][0] -1
posInLim = np.where(res[:,3] < 0.18)[0][0] -1
ax.plot(res[:,0],res[:,3])
ax.axhline(y=res[negInLim,3], color='black', linewidth=0.5, linestyle='--', label="VINmin = " + "%.2f" % (res[negInLim,0]*1e3) + " mV")
ax.axhline(y=res[posInLim,3], color='black', linewidth=0.5, linestyle='--', label="VINmax = " + "%.2f" % (res[posInLim,0]*1e3) + " mV")
ax.axvline(x=res[negInLim,0], color='black', linewidth=0.5, linestyle='--', label="VOUTmax = " + "%.2f" % res[negInLim,3] + " V")
ax.axvline(x=res[posInLim,0], color='black', linewidth=0.5, linestyle='--', label="VOUTmin = " + "%.2f" % res[posInLim,3] + " V")
print("%.2f" % res[posInLim,3])
ax.set_ylabel("Vout [V]")
plt.xlabel("Vin [mV]")
plt.legend()
plt.show()
