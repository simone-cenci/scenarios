import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import rcParams
from matplotlib import cm

rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Verdana']

'''
This code generates a visualisation of the exceedance probability data from the 
Sixth Assessment Report (AR6) of Working Group III 
by the Intergovernmental Panel on Climate Change (IPCC), entitled Climate Change 2022: Mitigation of Climate Change.
'''

#%%
def make_AR():
    #=== Load the data
    x = pd.read_csv("AR6_excess/ar6_snapshot_1667831078.csv")

    #===
    res = pd.DataFrame()
    for i in range(2020,2101):
        res = pd.concat((res, x[[str(i), 'Model', 'Scenario']].groupby(['Model', 'Scenario']).mean()), axis = 1)
    m = pd.DataFrame()
    for i in range(len(res)):
        scenario_name_clean = res.index[i][1].replace('_', ' ')
        m[scenario_name_clean] = res.iloc[i]
    sorted_ = m.mean().sort_values()
    m = m[sorted_.index]
    m = m*100
    cmap = cm.get_cmap('RdYlGn_r')
    ms = 8
    lw=4
    #=== Empty plot
    plt.figure(figsize = (12,8))
    ax = plt.subplot()
    plt.margins(x=0)
    plt.ylabel(r'Exceedance probability (1.5$^{\circ}$C), %')
    plt.axhline(y= 50, c = 'b', ls = '-.', lw =1)
    plt.ylim(0,100)
    ax.set_yticks(list(ax.get_yticks()) + [50])
    plt.xlim(2020, 2100)
    plt.xlabel('Year')


    #=== Worst case scenario
    plt.figure(figsize = (12,8))
    ax = plt.subplot()
    m['NGFS2 Current Policies'].plot(lw = lw,c = cmap(3*(1-1/9)), ax = ax, marker = 'o', ms = ms)
    plt.legend(loc = 'center left', bbox_to_anchor = (1,0.85))
    plt.margins(x=0)
    plt.ylabel(r'Exceedance probability (1.5$^{\circ}$C), %')
    plt.axhline(y= 50, c = 'b', ls = '-.', lw =1)
    ax.set_yticks(list(ax.get_yticks()) + [50])
    plt.ylim(0,100)
    plt.xlabel('Year')


    #=== Best case scenario
    plt.figure(figsize = (12,8))
    ax = plt.subplot()
    m['NGFS2 Current Policies'].plot(lw = lw,c = cmap(3*(1-1/9)), ax = ax, marker = 'o', ms=ms)
    m['SusDev SDP-PkBudg1000'].plot(lw = lw,c = cmap(0.025), ax = ax, marker = 'o', ms=ms)
    plt.legend(loc = 'center left', bbox_to_anchor = (1,0.85))
    plt.margins(x=0)
    plt.ylabel(r'Exceedance probability (1.5$^{\circ}$C), %')
    plt.axhline(y= 50, c = 'b', ls = '-.', lw =1)
    ax.set_yticks(list(ax.get_yticks()) + [50])
    plt.ylim(0,100)
    plt.xlabel('Year')



    #=== Middle case scenario
    plt.figure(figsize = (12,8))
    ax = plt.subplot()
    m['NGFS2 Current Policies'].plot(lw = lw,c = cmap(3*(1-1/9)), ax = ax, marker = 'o', ms=ms)
    m['SusDev SDP-PkBudg1000'].plot(lw = lw,c = cmap(0.025), ax = ax, marker = 'o', ms=ms)
    m['EN NPi2020 900f'].plot(lw = lw,c = cmap(0.78), ax = ax, marker = 'o', ms = ms)

    plt.legend(loc = 'center left', bbox_to_anchor = (1,0.85))
    plt.margins(x=0)
    plt.ylabel(r'Exceedance probability (1.5$^{\circ}$C), %')
    plt.axhline(y= 50, c = 'b', ls = '-.', lw =1)
    ax.set_yticks(list(ax.get_yticks()) + [50])
    plt.ylim(0,100)
    plt.xlabel('Year')



    #=== All models
    plt.figure(figsize = (12,8))
    ax = plt.subplot()
    m.plot(lw = lw,colormap = 'RdYlGn_r', ax = ax, marker = 'o', ms=ms)
    s = pd.DataFrame(m.mean(axis = 1))
    d = pd.DataFrame(m.std(axis = 1))/np.sqrt(len(m.columns))
    
    s.columns = ['Average']
    s.plot(lw = 3, ls = '-.', c = 'k', ax = ax)
    plt.fill_between(s.index, s.values.ravel()+d.values.ravel(),\
                     s.values.ravel()-d.values.ravel(), color= 'k', alpha = 0.5)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc = 'center left', bbox_to_anchor = (1,0.5))
    plt.margins(x=0)
    plt.ylabel(r'Exceedance probability (1.5$^{\circ}$C), %')
    plt.axhline(y= 50, c = 'b', ls = '-.', lw =1)
    ax.set_yticks(list(ax.get_yticks()) + [50])
    plt.ylim(0,100)
    plt.xlabel('Year')


    
#%%
if __name__ == '__main__':
    make_AR()
