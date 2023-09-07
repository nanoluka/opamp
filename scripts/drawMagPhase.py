import numpy as np
import matplotlib.pyplot as plt

def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)

filename = 'miel21_tb_opamp_ac.res'

res = np.loadtxt(filename,skiprows=1)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(res[:,0],res[:,1],color='green', label="AdB0 = " + "%.2f" % res[0,1] + " dB")
ax1.set_ylabel("Magnitude [dB]")
ax1.set_ylim([-20,60])

zeroMag = np.zeros(len(res[:,0]))

OmegaT = np.where(res[:,1] < 0)[0][0] 
f3dB = np.where(res[:,1] < res[0,1]-3)[0][0]
#print(f3dB)
#print(OmegaT)
ax1.axhline(y=res[f3dB,1], color='black', linewidth=0.5, linestyle="--", label="f3dB = " + "%.2f" % (res[f3dB,0]/1e6) + " MHz")
ax1.plot(res[:,0],zeroMag, color='black', linewidth=0.5, linestyle="--", label="fT = " + "%.2f" % (res[OmegaT,0]/1e6) + " MHz")
ax1.axvline(x=res[OmegaT,0], color='black', linewidth=0.5, linestyle="--", label="PM = " + "%.2f" % res[OmegaT,2] + " deg")
ax2.plot(res[:,0],res[:,2], label = "Phase [deg]")
ax2.set_ylabel("Phase [deg]")
ax2.set_ylim([-200,200])
ax1.set_xlabel("Frequency [Hz]")
ax1.set_xscale('log')
ax1.set_xlim([1,10e10])
ax1.legend(loc='lower left')
#align_yaxis(ax1, 0, ax2, 0)
plt.show()
