from math import *
import numpy as np
import time as t
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

j = 1
L = 1
dx = 1./100
dy = dx
CFL = 0.25
dt = CFL* dx
iter_max = 1000
##u_0 = np.exp(-np.power(np.linspace(0,L,L/dx)-0.5, 2.) / (2 * np.power(0.1, 2.)))*np.sin(20*pi*np.linspace(0,L,L/dx))
##u_0 = np.matrix([np.sin(2*pi*np.linspace(0,L,L/dx))]).transpose()*np.matrix([np.sin(2*pi*np.linspace(0,L,L/dx))])
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, L, dx)
Y = np.arange(0, L, dy)
X, Y = np.meshgrid(X, Y)
##u_0 = np.sin(2*pi*X)*np.sin(2*pi*Y)
a=10
u_0 = np.exp(-a*((X-0.75)**2+(Y-0.75)**2))
print(u_0.shape)
surf = ax.plot_surface(X,Y,u_0, cmap=cm.coolwarm)
plt.title("Condition Initiale")
plt.show()


u_1 = u_0.copy()
u_next = u_0.copy()
u_precedent = u_0.copy()
u_actuel = u_1.copy()
nb_iter = int(L/dx) #nb iterations en espace
##ax = fig.add_subplot(111, projection='3d')
##ax.plot_surface(np.linspace(0,L,L/dx),np.linspace(0,L,L/dx),u_0)



while j < iter_max :
  j=j+1
  u_next[1:nb_iter-2,1:nb_iter-2] = 1*(2*u_actuel[1:nb_iter-2,1:nb_iter-2]-u_precedent[1:nb_iter-2,1:nb_iter-2]+
                                          (dt**2)/(dx**2)*(u_actuel[2:nb_iter-1,1:nb_iter-2]-2*u_actuel[1:nb_iter-2,1:nb_iter-2]+u_actuel[0:nb_iter-3,1:nb_iter-2])+
                                          (dt**2)/(dx**2)*(u_actuel[1:nb_iter-2,2:nb_iter-1]-2*u_actuel[1:nb_iter-2,1:nb_iter-2]+u_actuel[1:nb_iter-2,0:nb_iter-3]))

  u_next[1:nb_iter-2,0] = 1*(2*u_actuel[1:nb_iter-2,0]-u_precedent[1:nb_iter-2,0]+
                                          (dt**2)/(dx**2)*(u_actuel[2:nb_iter-1,0]-2*u_actuel[1:nb_iter-2,0]+u_actuel[0:nb_iter-3,0])+
                                          (dt**2)/(dx**2)*(u_actuel[1:nb_iter-2,0]-2*u_actuel[1:nb_iter-2,0]+u_actuel[1:nb_iter-2,nb_iter-1]))
  u_next[1:nb_iter-2,nb_iter-1] = 1*(2*u_actuel[1:nb_iter-2,nb_iter-1]-u_precedent[1:nb_iter-2,nb_iter-1]+
                                          (dt**2)/(dx**2)*(u_actuel[2:nb_iter-1,nb_iter-1]-2*u_actuel[1:nb_iter-2,nb_iter-1]+u_actuel[0:nb_iter-3,nb_iter-1])+
                                          (dt**2)/(dx**2)*(u_actuel[1:nb_iter-2,0]-2*u_actuel[1:nb_iter-2,nb_iter-1]+u_actuel[1:nb_iter-2,nb_iter-1]))
  u_next[0,1:nb_iter-2] = 1*(2*u_actuel[0,1:nb_iter-2]-u_precedent[0,1:nb_iter-2]+
                                          (dt**2)/(dx**2)*(u_actuel[0,1:nb_iter-2]-2*u_actuel[0,1:nb_iter-2]+u_actuel[nb_iter-1,1:nb_iter-2])+
                                          (dt**2)/(dx**2)*(u_actuel[0,2:nb_iter-1]-2*u_actuel[0,1:nb_iter-2]+u_actuel[0,0:nb_iter-3]))
  u_next[nb_iter-1,1:nb_iter-2] = 1*(2*u_actuel[nb_iter-1,1:nb_iter-2]-u_precedent[nb_iter-1,1:nb_iter-2]+
                                          (dt**2)/(dx**2)*(u_actuel[0,1:nb_iter-2]-2*u_actuel[nb_iter-1,1:nb_iter-2]+u_actuel[nb_iter-1,1:nb_iter-2])+
                                          (dt**2)/(dx**2)*(u_actuel[nb_iter-1,2:nb_iter-1]-2*u_actuel[nb_iter-1,1:nb_iter-2]+u_actuel[nb_iter-1,0:nb_iter-3]))
   
  u_precedent = u_actuel
  u_actuel = u_next

  if j % 100 == 0 :
    fig2 = plt.figure()
    ax2 = fig2.gca(projection='3d')
    plotlabel= "N = " + str(j) 
    surf = ax2.plot_surface(X,Y,u_actuel, cmap=cm.coolwarm)
    ax2.set_zlim(-1.01, 1.01)
    #plt.clim(-0.1,0.1)
    plt.title(plotlabel)
    plt.draw()

  plt.show()

# print(u_actuel)
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# surf = ax.plot_surface(X,Y,u_actuel, cmap=cm.coolwarm)
# plt.show()
