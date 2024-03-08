"""
Necessary functions to treat the Spherical Harmonics data from a measured bead , 
evaluate the stress tensor and plot the results

"""
import sympy as sp
import pyshtools as sh
from pyshtools.shio import SHrtoc
import numpy as np
from sympy import IndexedBase, lambdify
from time import time
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib import cm
import dill 
from matplotlib.ticker import MaxNLocator

#plt.close('all')
dill.settings['recursive']=True
r, r0, theta, phi, l, m, pi, x, nu, G = sp.symbols('r, r0, θ, φ, l, m, π, x, ν, G')

# Two simple function to separate real and img
take_real = np.vectorize(np.real)
take_imag = np.vectorize(np.imag)


def ComplexCoeffs(coeff_table):
    '''
    Converts a table of real Spherical Harmonics coefficients to 
    complex form. 
    The normalization of the spherical harmonics is maintained,
    as well as the Condon-Shortley convention 
    '''
    table_split_mpos = SHrtoc(coeff_table)
    table_mpos = table_split_mpos[0]+1j*table_split_mpos[1]
    rs, cs = np.shape(table_mpos)
    m_buffer = np.repeat(np.array(range(0,cs)), rs, axis=0).reshape(cs,rs).T
    table_mneg =  np.conj(table_mpos) *(-1)**(m_buffer)
    table = np.stack((table_mpos, table_mneg), axis=0)
    
    return table


def create_table(filepath, mode='npy', units='um'):
    '''
    Creates a table of Spherical Harmonics coefficients, both in real and complex
    form (for calculations and plots purposes respectively) from a saved file.
    It can read both .npy python structures and .txt files, as decided by the argument 
    "mode".
    Additionaly, it returns the original bead radius and the order of decomposition lmax.
    For the purpose of the stress tensor calculation with Lea Krueger's theory, the normalization 
    has been hardcoded to 'orthonormal'.
    '''
    if mode=='npy':
        coeffs = sh.SHCoeffs.from_file(filepath, format='npy', normalization='ortho', csphase=-1)
        coeff_table_real = coeffs.coeffs
    
    elif mode=='txt':
        with open (filepath, 'r') as f:
            data = [list(map(float,line.split(' '))) for line in f if ('Positive' not in line and 'Negative' not in line)]
            m_pos = np.array(data[0:int(len(data)/2)])
            m_neg = np.array(data[int(len(data)/2):])
            coeff_table_real = np.array([m_pos, m_neg])
            coeffs = sh.SHCoeffs.from_array(coeff_table_real, normalization='ortho', csphase=-1)
    
    # Common operations for both formats
    lmax = np.shape(coeff_table_real)[1]-1
    # Original volume and d00
    d00_prime = float(coeff_table_real[0,0,0])
    volume = coeffs.convert(normalization='4pi').volume()
    initial_radius = np.cbrt(3*volume/(4*np.pi))
    # We need to truncate to avoid small contributions from delta-volume
    d00 = np.round(d00_prime-initial_radius*np.sqrt(4*np.pi), 12)
    # Substitute d00 for the [0,0,0] value in the complex table 
#    coeff_table_complex[0,0,0] = complex(d00)
    coeff_table_real[0,0,0] = d00
    coeff_table_complex = ComplexCoeffs(coeff_table_real)

    # Convert to SI units
    if units =='m':
        coeff_table_real = coeff_table_real*1e-6
        coeff_table_complex = coeff_table_complex*1e-6
        initial_radius = initial_radius*1e-6
        
    return lmax, coeff_table_real, coeff_table_complex, initial_radius


def SubsSHCoeffs(expr, coeff_table, Order, first_n=0): 
    '''
    Substitutes all the Spherical Harmonic coefficients from a table into a
    pre-existing sympy expression of the Stress Tensor.
    We always have coefficients of nmax+2, if nmax was the max order of our equation
    For performance purposes, the value of all coeffs are stored in a dictionary 
    and substituted simultaneously
    '''
    D = IndexedBase('D')
    start = time()
    maxn = np.shape(coeff_table)[1]
    substs = {}
    for n in tqdm(range(first_n, Order+3), colour='cyan'): #Order+2 will be necessary
        for m in range(-n, n+1):
            if n>=maxn: # if the coefficient is not in our table
                substs[D[n,m]] = 0
            elif m >=0:
                substs[D[n,m]] = coeff_table[0,n,m]
            else:
                substs[D[n,m]] = coeff_table[1,n,-m]
    expr = expr.subs(substs) # Simultaneous substitution
    print(f'\nSubstitution of SH coefficients took {int(time()-start)} seconds')
    return expr.evalf()

def Equation2Maps(sympy_expression, coeff_table, initial_radius, resolution=15):
    '''
    This functions takes a sympy expression of the Stress Tensor (with the Spherical
    Harmonics coefficients and the physical parameters already substituted) and converts
    it to a set of maps (radius, stress tensor) in latitude-longitude spherical projections.
    The input expression must only be dependent on {r, θ, φ}, i.e. the spatial coordinates
    
    When using the current convention, 
    * longitutes (phi) span [0...2pi]
    * latitudes (theta) span [0...pi]
    '''
    coeffs = sh.SHCoeffs.from_array(coeff_table, normalization='ortho',csphase=-1)
    coeffs.lmax = resolution 
    grid = coeffs.expand() 
    map_deform = grid.to_array()
    map_r = map_deform + initial_radius 
    # there is a small imaginary contribution from rounding errors
    map_r_R = take_real(map_r) 
    map_deform = take_real(map_deform)
    map_deform_norm = map_deform/initial_radius
    
    pp, tt = np.meshgrid(
            grid.lons()*np.pi/180,
            np.flip(grid.lats()*np.pi/180 + np.pi/2))
            #grid.lats()*np.pi/180)
#    print(f'Phi spans from {np.amin(pp)} to {np.amax(pp)}')
#    print(f'Theta spans from {np.amin(tt)} to {np.amax(tt)}')       
        
    T_function = lambdify([r, theta, phi], sympy_expression)
    T_complex = T_function(map_r_R, tt, pp) 
    map_T_real = take_real(T_complex)
    map_T_imag = take_imag(T_complex)
    
    return map_deform_norm, map_r_R, map_T_real, map_T_imag


def Plotter_Maps2D(maps,titles=[], units=[]):
    """
    This function accepts a list with an arbitraty number of maps to be plotted
    and plots them in latitude-longitude fashion
    """
    plt.style.use('dark_background')
    fuente = {'fontsize':12, 'fontname':'Arial'}
    N_maps = len(maps)
    len_tt, len_pp = np.shape(maps[0])[0]-1, np.shape(maps[0])[1]-1
    fig, axM = plt.subplots(N_maps, 1, sharex=True, figsize=(6,6))
    print(f'Titles: {titles}')
    if N_maps==1:
        axM=[axM]
    
    for i, amap in enumerate(maps):
        m = axM[i].imshow(amap, cmap='RdBu')#, vmin=-0.5, vmax=0.5)  # custom range     
        axM[i].set_xticks([0,int(len_pp/2),len_pp])
        axM[i].set_yticks([0,int(len_tt/2),len_tt])
        axM[i].set_yticklabels([r'$0$', r'$\pi/2$', r'$\pi$'])
        axM[i].set_ylabel(r'$\theta$', **fuente)        
        cbar = plt.colorbar(m, ax=axM[i], fraction=0.024, pad=0.04)
        cbar.formatter.set_powerlimits((0, 0)) # so that we have scientific notation
        
        if len(units)==len(maps):
            cbar.ax.set_ylabel(units[i])
            
        if len(titles)==N_maps:
            #for i,title in enumerate(titles):
            axM[i].set_title(titles[i],**fuente)
        
    axM[N_maps-1].set_xlabel(r'$\phi$')
    axM[N_maps-1].set_xticklabels(['0', r'$\pi$', r'$2\pi$'])
    plt.show()
    
# Forcing normalization of facecolor to match the 2D plots    
#from matplotlib import colors
#norm = colors.Normalize(-0.5, 0.5)
    
def Plotter_MapOnMap(map_r, map_toplot, title='', axs=None):
    """This calculates the bead shape and plots the facecolor 
    of the surface proportional to the second map provided"""
    #fuente = {'fontsize':8, 'fontname':'Arial'}
    map_shape = np.shape(map_r) 
    # Coordinates
    pp, tt = np.meshgrid( 
    np.linspace(0, 2*np.pi, map_shape[1]),
    np.linspace(0, np.pi, map_shape[0]))   
    x = map_r * np.sin(tt) * np.cos(pp)
    y = map_r * np.sin(tt) * np.sin(pp)
    z = map_r * np.cos(tt)
    #Plot with custom map as facecolor
    #plt.style.use('dark_background')
    
    # The axes are already existing, either externally or in the GUI
    axs.set_title(title)#,**fuente)
    axs.plot_surface(x,y,z,facecolors=cm.RdBu((map_toplot-np.amin(map_toplot))/(np.amax(map_toplot)-np.amin(map_toplot))))
    axs.set_xlabel(r'$\mu m$')#, **fuente)
    axs.set_ylabel(r'$\mu m$')#,**fuente)
    axs.set_zlabel(r'$\mu m$')#,**fuente)
    #ax.plot_surface(x,y,z,facecolors=cm.RdBu_r((map_toplot-np.amin(map_toplot))/(np.amax(map_toplot)-np.amin(map_toplot))))
    axs.plot_surface(x,y,z,facecolors=cm.RdBu((map_toplot-np.amin(map_toplot))/(np.amax(map_toplot)-np.amin(map_toplot))))
    #ax.plot_surface(x,y,z,facecolors=cm.plasma(norm(map_toplot)))
    
    # Transparent panes:
    axs.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    axs.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    axs.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    # Force integers in all axes
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.zaxis.set_major_locator(MaxNLocator(integer=True))
    axs.set_box_aspect((np.amax(x)-np.amin(x), np.amax(y)-np.amin(y), np.amax(z)-np.amin(z)))
    #plt.draw()
    
def IntegrateTension(map_r, map_T_real):
    '''
    This function numerically integrates the radial tension over the surface
    of the bead, as a sum of the product pairs Tension*SurfaceDifferential
    '''
    N_theta, N_phi = np.shape(map_r)
    dtheta, dphi = np.pi/N_theta, 2*np.pi/N_phi
    pp, tt = np.meshgrid( 
            np.linspace(0, 2*np.pi, N_phi),
            np.linspace(0, np.pi, N_theta)) 
    dF = map_T_real * map_r**2 * np.sin(tt) * dphi * dtheta
    F = sum(map(sum,dF))
    return F


#%%########################
###### MAIN FUNCTION ######
###########################
def BeadSolver(FolderPath, mode='txt', units='um', Order=3, nu_exp=0.491, G_exp=7800, 
               saveplots=False, force=False, show2D=False, axs3D=None):
    '''
    This function will look for a table called 'SH_Coefficients.txt' in the path and calculate
    the bead shape, the tension and the force on its surface, outputted as 2D and 3D maps
    It has been modified to work in conjunction with the GUI.
    show2D: whether a 2D map is shown externally or not
    axs3D: inm which axes the 3D map shoulb be shown
    '''
    #plt.close('all')
    print(f'Analytical solution of order {Order} ')
    start = time()
    params = {nu: nu_exp, G: G_exp} 
    #TablePath = FolderPath + '/SH_Coefficients.txt' 
    
    # Load dilled version of MasterEquation, substitute physical values
    filename = './Solutions_PYRAMID/GeneralSolutionDILLED_lmax='+str(Order).zfill(2)+'.txt'
    MasterEquation = dill.load(open(filename, 'rb'))
    MasterEquation = MasterEquation.subs(params)
    
    # Initialize parameters from table
    lmax, coeff_table_real, coeff_table_complex, initial_radius = create_table(FolderPath, mode=mode, units=units)
    
    # Substitute parameters and coefficients in equation
    Trr = SubsSHCoeffs(MasterEquation, coeff_table_complex, Order, first_n=0)
    Trr = Trr.subs(r0, initial_radius).evalf()
    
    # Create 2D maps
    map_deform_norm, map_r, map_T_real, map_T_imag = Equation2Maps(Trr, coeff_table_complex, initial_radius)

    # In any case, plot 3D in a chosen axis:
    Plotter_MapOnMap(map_r, map_T_real, axs=axs3D, title='Radial tension')
    # For GUI, if checked, 2D plots are also shown
    if show2D==True:
        Plotter_Maps2D([map_r, map_T_real], titles=['Radius', 'Radial tension'], units=[r'$\mu m$', '$Pa$'])
        
######################################
    # Finish and return
    print(f'Complete evaluation took {round((time()-start), 3)} seconds \n')


    if force==True:
        F = IntegrateTension(map_r, map_T_real)
        return map_T_real, F
    else: 
        return 
    
#%%
def SaveTension(map_T_real, Order,  savepath, npy=True, SH=True):
    """
    Function to save the results of tension both in a numpy structure and 
    in a table of Spherical Harmonics 
    """
    if npy==True:
        savename = savepath + f'TensionMap_2D_order={Order}.npy'
        np.save(savename, map_T_real)
    
    if SH==True:
        H, W = np.shape(map_T_real)
        lons, lats = np.meshgrid(np.linspace(0,360, W), np.linspace(90, -90, H))
        # Flatten the arrays bsfore feeding them to ShExxpand
        map_T_real, lons, lats = map_T_real.flatten(), lons.flatten(), lats.flatten()
        SHExp = sh.expand.SHExpandLSQ(map_T_real, lats, lons, lmax=10, norm=4)[0] # orthonormal
        savename = savepath + f'TensionMap_SHCoeffs_order={Order}.npy'
        np.save(savename, SHExp)                

#%% Example use
#import os
#MainPath = '/media/alejandro/Coding/MyGits/Derivation_StressTensor/ExampleBeads/'
#folders = [MainPath+subpath+'/' for subpath in os.listdir(MainPath)]
#
#for i, folder in enumerate(folders):
#    print('#####################################')
#    print(f'ANALYZING FOLDER {i} FROM {len(folders)}')
#    print('#####################################')
#    Forces = []
#    for n in range(1,11): 
#        map_T_real, force = BeadSolver(folder, mode='txt', units='m', Order=n, nu_exp=0.45, G_exp=1000, saveplots=True, force=True)
#        SaveTension(map_T_real,n, folder, npy=True, SH=True)
#        Forces.append(force)
#        
#    orders = np.arange(1,len(Forces)+1,1)
#    plt.figure()
#    plt.plot(orders, Forces,'-o', c='lime')
#    plt.xlabel('Order')
#    plt.ylabel('Force [N]')
#    plt.title('Force on the bead surface')
#    plt.savefig(folder+f'Force_{folder.split("/")[-2]}.png')
