from math import *
import numpy as np
import time as t
import matplotlib.pyplot as plt
import scipy as sc



## DECLARATION DES PARAMETRES
L = 3
c=1
dx = 1./400
CFL = 0.2
dt = CFL* dx
T = 5
Epsilon = 1.5
omega_0 = 20
alpha = 1

## AUTRES DECLARATIONS
j = 0 #compteur temps
i = 0 #compteur energie 
nbx=int(L/dx) #nb intervalles
iter_max = int(T/dt) #nb iterations
print(iter_max)
pas=200 #pas utilise pour affichage et calcul de l'energie
int_tab=np.zeros(int(iter_max/pas)+1) # tab energie

## INIT
x=np.linspace(-L,L,L/dx+1)
nb_iter = len(x) #nb iterations en espace
i_source = int(len(x)/2)+1
Sigma = np.maximum(np.zeros(len(x)),x**2-(L-Epsilon)**2)
p = np.zeros(len(x))
#p = np.exp(-np.power(x, 2.))
v = np.zeros(len(x))
v_next = v.copy()
p_next = p.copy()

while j<iter_max :
    j=j+1
    vg = np.concatenate((np.array([0]),v[0:nb_iter-1]))
    vd = np.concatenate((v[1:nb_iter],np.array([0])))
    pg = np.concatenate((np.array([0]),p[0:nb_iter-1]))
    pd = np.concatenate((p[1:nb_iter],np.array([0])))
   
    p_next = (1/(2*dx)*((vd-vg)+(pd-2*p+pg))+p/dt )/(np.ones(len(x))*1/dt+Sigma)
    v_next = (1/(2*dx)*((pd-pg)+(vd-2*v+vg))+v/dt )/(np.ones(len(x))*1/dt+Sigma)

    p_next[i_source]=alpha * sin(omega_0*j*dt)

    p=p_next
    v=v_next

    if j % pas == 0 :
    	i = i+1
        plotlabel= "N = " + str(j) + " ITER = " + str(i)
        plt.plot(x,p)
        plt.axis([-L, L, -1.2, 1])
        #plt.clim(-0.1,0.1)
        plt.title(plotlabel)
        plt.draw()

	plt.show()


    
    
    
