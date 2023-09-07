import numpy as np
import matplotlib.pyplot as plt

filename = 'miel21_tb_opamp_tran.res'

res = np.loadtxt(filename,skiprows=1)

fig, ax = plt.subplots(2)
ax[0].plot(res[:,0]*1e6,(res[:,1]-res[:,2])*1e3, label = "VINamplitude = 1 mV")
ax[0].legend(loc='lower right')
ax[0].set_ylim([-2,2])
ax[0].set_ylabel("Vin [mV]")
outA = np.max(res[:,3]) - np.min(res[:,3])
ax[1].plot(res[:,0]*1e6,res[:,3], color='green', label="VOUTamplitude = " + "%.2f" % (outA/2) + " V")
plt.legend(loc='lower right')
ax[1].set_ylim([1.5,2.4])
ax[1].set_ylabel("Vout [V]")
plt.xlabel("Time [us]")

plt.show()
