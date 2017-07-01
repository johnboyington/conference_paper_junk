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
plt.title('NEBP Filtered Neutron Spectrum')
plt.xlabel('Energy ($MeV$)')
plt.ylabel('Relative Flux')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1E-8, 1E1)
plt.ylim(1E-8, 1E1)

#load neutron simulation data
n_data = np.loadtxt('ndata.txt')



#energy groups
number_of_erg_groups = len(n_data[:,0])
erg_groups = n_data[0:number_of_erg_groups,0]
erg_group_width = erg_groups[1:] - erg_groups[:-1]
erg_bin_centers = (erg_groups[1:] + erg_groups[:-1]) / 2

#flux & error data stored in [angle,group] format
n_flux = n_data[1:,1]
n_error = n_data[1:,2]
n_tot = np.sum(n_flux)
n_flux *= n_tot

#simple plot

plt.plot(makeStep(erg_groups, n_flux)[0], 
         makeStep(erg_groups, n_flux / erg_group_width)[1])
plt.errorbar(erg_bin_centers, n_flux / erg_group_width, n_error * (n_flux / erg_group_width),
             linestyle="None", capsize=0)
#plt.plot(makeStep(erg_groups, n_flux)[0], 
#         makeStep(erg_groups, n_flux)[1])
#plt.errorbar(erg_bin_centers, n_flux, n_error * (n_flux),
#             linestyle="None", capsize=0)
plt.savefig('Flux_vs_Energy_nebp_filtered.png')