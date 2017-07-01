'''
This code will take any energy grouped, stripped data and plot it.
'''

import numpy as np
import matplotlib.pyplot as plt


#makes plt.plot data out of step data
def makeStep(x,y):
    #assert len(x) - 1== len(y)
    Y = np.array([[yy,yy] for yy in np.array(y)]).flatten()
    X = np.array([[xx,xx] for xx in np.array(x)]).flatten()[1:-1]
    return X,Y



plt.figure(0)
plt.xlabel('Energy ($MeV$)')
plt.ylabel('$\phi(E)$')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1E-8, 1E1)
plt.xticks(np.logspace(-8, 1, 10))
plt.tick_params(axis='both', which='minor', bottom='off', top='off', left='off', right='off', labelbottom='off')

plt.figure(1)
plt.xlabel('Energy ($MeV$)')
plt.ylabel('$\phi(E) E$')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1E-8, 1E1)
plt.xticks(np.logspace(-8, 1, 10))
plt.tick_params(axis='both', which='minor', bottom='off', top='off', left='off', right='off', labelbottom='off')

#load neutron simulation data
for data in ['source_ndata.txt', 'ndata.txt']:
    n_data = np.loadtxt(data)



    #energy groups
    number_of_erg_groups = len(n_data[:,0])
    erg_groups = n_data[0:number_of_erg_groups,0]
    erg_group_width = erg_groups[1:] - erg_groups[:-1]
    erg_bin_centers = (erg_groups[1:] + erg_groups[:-1]) / 2

    #flux & error data stored in [angle,group] format
    n_flux = n_data[1:,1]
    n_error = n_data[1:,2]
    n_tot = np.sum(n_data[:,1])
    #if data == 'ndata.txt': n_flux *= 6.76356E-3
    if data == 'source_ndata.txt': n_flux /= 2.3823E-6
    #n_flux *= 3.324E7 * 250

    #simple plot
    if data == 'ndata.txt': 
        label='Filtered Spectrum' 
        color='mediumseagreen'
    if data == 'source_ndata.txt': 
        label='Source Spectrum' 
        color='mediumblue'
    plt.figure(0)
    plt.plot(makeStep(erg_groups, n_flux)[0], 
             makeStep(erg_groups, n_flux / erg_group_width)[1],
             label='{}'.format(label),
             color=color)
    plt.errorbar(erg_bin_centers, n_flux / erg_group_width, n_error * (n_flux / erg_group_width),
                 linestyle="None", capsize=0,
                 color=color)
    
    plt.figure(1)
    plt.plot(makeStep(erg_groups, n_flux)[0], 
             makeStep(erg_groups, erg_bin_centers * (n_flux / erg_group_width))[1], 
             label='{}'.format(label),
             color=color)
    plt.errorbar(erg_bin_centers, erg_bin_centers * n_flux / erg_group_width, erg_bin_centers * n_error * (n_flux / erg_group_width),
                 linestyle="None", capsize=0,
                 color=color)

plt.figure(0)
plt.legend()
plt.savefig('Flux_vs_Energy.png', dpi=200)
plt.figure(1)
plt.legend()
plt.savefig('Flux_vs_Energy_lethargy.png', dpi=200)
