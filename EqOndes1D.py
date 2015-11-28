from math import *
import numpy as np
import time as t
import matplotlib.pyplot as plt
import scipy as sc



## DECLARATION DES PARAMETRES
L = 1
c=1
dx = 1./500
CFL = 0.2
dt = CFL* dx
T = 1

## AUTRES DECLARATIONS
j = 0 #compteur temps
i = 0 #compteur energie 
nb_iter = L/dx #nb iterations en espace
nbx=int(L/dx) #nb intervalles
iter_max = int(T/dt) #nb iterations
print(iter_max)
pas=200 #pas utilise pour affichage et calcul de l'energie
int_tab=np.zeros(int(iter_max/pas)+1) # tab energie


## INIT
x=np.linspace(0,L,L/dx)
u_0 = np.exp(-np.power(x-0.5, 2.) / (2 * np.power(0.1, 2.)))*np.sin(20*pi*x)
##u_0 = np.sin(2*pi*x)
#u_1 = u_0
u_next = u_0.copy()
u_precedent = u_0.copy() # ici jai un doute puisquon met u pred et u actuel a la meme valeur pour la premiere iter 
u_actuel = u_0.copy()



while j<iter_max :
    j=j+1
    u_next[1:nb_iter-2] = 2*u_actuel[1:nb_iter-2]-u_precedent[1:nb_iter-2]+ (c**2)*(dt**2)/(dx**2)*(u_actuel[2:nb_iter-1]-2*u_actuel[1:nb_iter-2]+u_actuel[0:nb_iter-3])
    u_next[0] = 2*u_actuel[0]-u_precedent[0]+ (c**2)*(dt**2)/(dx**2)*(u_actuel[1]-2*u_actuel[0]+u_actuel[nb_iter-1])
    u_next[nb_iter-1] = 2*u_actuel[nb_iter-1]-u_precedent[nb_iter-1]+(c**2)*(dt**2)/(dx**2)*(u_actuel[0]-2*u_actuel[nb_iter-1]+u_actuel[nb_iter-2])
    u_precedent = u_actuel.copy()
    u_actuel = u_next.copy()

    
    if j % pas == 0 :
    	i = i+1
    	##calcul aire
    	integrale=0
    	for k in range(nbx-1):
    		integrale = integrale + u_actuel[k]*(x[k+1]-x[k])
    	print(integrale)
    	int_tab[i] = integrale
        plotlabel= "N = " + str(j) + " ITER = " + str(i)
        plt.plot(x,u_actuel)
        plt.axis([0, L, -1.2, 1.2])
        #plt.clim(-0.1,0.1)
        plt.title(plotlabel)
        plt.draw()

	plt.show()

fig2=plt.figure(2)
plt.plot(int_tab)
plt.show()
    
    
    
