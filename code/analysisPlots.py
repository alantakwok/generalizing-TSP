'''Creates analysis plots and saves them to the folder.'''
import numpy as np
from analysis import analysis
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties()
#font.set_family('sans-serif')
font.set_name('Roboto')

(time11,time13,time15,time16,time17,time18,time19,ratioarray) = analysis()
sampleSize = [100,100,100,100,70,40,10]
nList = np.array([11,13,15,16,17,18,19])

# time statistics
timeStats = np.zeros((7,6))
timeList = [time11,time13,time15,time16,time17,time18,time19]
dummy = 0
for n in timeList:
    (tsp,dp) = (n[:,0],n[:,1])
    timeStats[dummy,0:3] = [np.mean(tsp),np.std(tsp),np.amax(tsp)]
    timeStats[dummy,3:] = [np.mean(dp),np.std(dp),np.amax(dp)]
    dummy += 1

# time plot
(mean_tsp,mean_dp) = (timeStats[:,0],timeStats[:,3])
x = np.arange(7)
width = 0.333
fig1, ax1 = plt.subplots()
plt.grid(True)
rects = ax1.bar(nList-width,mean_tsp,width,color='tab:red',label='TSP',zorder=3)
rects = ax1.bar(nList,mean_dp,width,color='tab:blue',label='DP',zorder=3)
ax1.set_xticks(nList-width/2,nList, fontproperties=font)
plt.legend(loc='upper left',prop=font)
plt.yticks(fontproperties=font)
plt.yscale("log")
plt.xlabel("n", fontproperties=font)
plt.ylabel("Computation time (seconds)", fontproperties=font)
ax1.grid(zorder=0)
plt.savefig('../figures/time_compare.png',dpi=600,bbox_inches='tight', pad_inches=0.05)
plt.show()

# distribution plot: dp/tsp
fig2, ax2 = plt.subplots()
ax2.hist(np.round(ratioarray[:,0],2), range=(0.85,1.01),bins=16,zorder=3,edgecolor="white",cumulative=True,density=True)
ax2.grid(zorder=0)
plt.xlabel("DP / TSP", fontproperties=font)
plt.ylabel("Cumulative frequency", fontproperties=font)
ax2.set_xticks(np.linspace(0.85,1,4),np.linspace(0.85,1,4), fontproperties=font)
plt.xticks(fontproperties=font)
plt.yticks(fontproperties=font)
plt.savefig('../figures/dp-vs-tsp.png',dpi=600,bbox_inches='tight', pad_inches=0.05)
plt.show()

# heuristics plots
fig3, ax3 = plt.subplots()
ax3.boxplot(ratioarray[:,1:],positions=[2,4,6,8],widths=1.5,zorder=3,whis=(2.5,97.5),medianprops={"color": "tab:red"})
ax3.grid(zorder=0)
plt.xlabel("Heuristic", fontproperties=font)
plt.ylabel("Value / DP", fontproperties=font)
ax3.set_xticks([2,4,6,8],['TSP', 'DP-MST', 'DP-MST-half', 'DP-MST-3opt'])
plt.xticks(fontproperties=font)
plt.yticks(fontproperties=font)
plt.savefig('../figures/heuristics.png',dpi=600,bbox_inches='tight', pad_inches=0.05)
plt.show()
