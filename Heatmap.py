# Heatmap with Color Bar
# MBD2-p66a inhibitor discovery
# Python 3.4
# Insung Na. 10/12/2016

import matplotlib.pyplot as plt
import numpy as np

def main():

    DATA = open('./Com2_NormalizedContNumbers.txt', 'r')
    DATA_rl = DATA.readlines()
    DATA.close()

    A = [float(x) for x in DATA_rl[0].replace('\n','').split('\t')]
    B = [float(x) for x in DATA_rl[1].replace('\n','').split('\t')]
    C = [float(x) for x in DATA_rl[2].replace('\n','').split('\t')]
    D = [float(x) for x in DATA_rl[3].replace('\n','').split('\t')]

    Input = [A, B, C, D]
    myarray = np.asarray(Input)
    print(myarray)
    data = myarray
    rows = list('Conditions')
    columns = list('Residues')
    fig, ax = plt.subplots()
    ax.pcolor(data,cmap=plt.cm.Blues,edgecolors='k')
    xt = np.arange(0,43)+0.5
    xlabel = np.arange(0,43)
    ylabel = ['1','2','3','4']
    yt = np.arange(0,5)+0.5
    ax.set_xticks([])
    ax.set_yticks([])
    #ax.set_xticks(xt)
    #ax.set_yticks(yt)
    #ax.xaxis.tick_top()
    #ax.yaxis.tick_left()
    ax.invert_yaxis()
    plt.xlim(0,43)
    #plt.yticks(yt,ylabel,fontweight='bold')
    #plt.xticks(xt,xlabel,fontweight='bold')
    #plt.ylabel('Y Axis Label',fontsize=10,fontweight='bold')
    #plt.xlabel('X Axis Label',fontsize=10,fontweight='bold')

    # Color Bar
    p = ax.pcolormesh(data,cmap=plt.cm.Blues)
    box = ax.get_position()
    axColor = plt.axes([box.x0*1.05 + box.width*1.05, box.y0, 0.01, box.height])
    # plt.colorbar(p, cax = axColor, orientation="vertical")
    v = np.linspace(start=0, stop=0.8, num=5, endpoint=True)
    cbar = plt.colorbar(p, cax=axColor, orientation="vertical", ticks=v)

    plt.show()
    plt.subplot(aspect='equal')
    plt.close()

main()
