import numpy as np
import matplotlib.pyplot as plt
import time             # added time. Used in testing and gave me an idea of runtime

# a basic rk4 routine implemented in octave
#  based on an rk4 routine from:
# https://math.okstate.edu/people/yqwang/teaching/math4513_fall11/Notes/rungekutta.pdf

# the code has been modified to use arbitrary function names, return
# output in an array, and have vectors of an arbitrary length for
# its input



def projectile(time, p): 
    x = p[0]
    z = p[1]
    vx = p[2]
    vz = p[3]

    # This is a 2trick to set the projectile constants as initial conditions 
    coeff = p[4] 

    drv = np.zeros(5, np.float)

    # the velocities are the derviative of position
    drv[0] = vx
    drv[1] = vz


    # calcualte the acceleration
    g = -9.8  # m/s - gravity
  
    ax = -coeff * vx * vx * np.sign(vx) 
    az = g  - np.sign(vz) * coeff * vz*vz


    # update the change vector
    drv[2] = ax
    drv[3] = az

    # we don't actually update the projectile constants since they are constant
    drv[4] = 0

    return drv

def myrungekutta(h, t, nsteps, y0):
    # rk4 routine  
    # inputs:
    #   h      - stepsize (dt)
    #   t      - starting time for the integration
    #   nsteps - number of steps to take during the integration
    #   y0     - initial conditions for the equation
    #
    #  outputs:
    #  output:  an array of the output values of system
    y = y0
    # find the number of values in the initial conditions array
    ny = len(y)
    output = np.zeros([1,ny+1], np.float)
    YCheck = 'False'
    
    # loop over the array and calculate the position using an rk4
    # ODE integration routine
    for i in range(nsteps):
        while YCheck == 'False':
            k1 = h*projectile(t,y)
            k2 = h*projectile(t+h/2, y+k1/2)
            k3 = h*projectile(t+h/2, y+k2/2)
            k4 = h*projectile(t+h, y+k3)
            y = y + (k1 + 2*(k2+k3) + k4)/6
            t = t + h

            output[i,0] = t
            output[i,1:] = y[:]
        
            if output[:,2][i] <= 0:     # added this to get only successful launches
                YCheck = 'True'
        
    return output

##################

##################
# integration parameters  

# initial position and air resistance
x =0
z =0
coeff = 0.005

# inputs are 
#  v- initial velocity of the projectile
#  theta - the angle above the ground
#  h = step size - generally below one
#  tfinal - final time in the simulation

h = float(0.0001)
tfinal = float(20.00)

# number of steps; irrelevant. choose something small
nsteps = int(tfinal / h) + 1

t = 0.0001

aResults = []
xResults = []
tResults = []

start_time = time.time()
for a in range(1, 90):
    for xv in np.arange(1, 381, 0.25):
        theta = a
        v = xv
        
        #v, theta, h, tfinal = input()
        
        vx = np.cos(theta * np.pi / 180.) * v
        vz = np.sin(theta * np.pi / 180.) * v
        
        # initial conditions for a circular projectile of unit size
        
        p0 = [x, z, vx, vz, coeff]
        
        o = myrungekutta(h, t, nsteps, p0)
        
        if o[:,1] >= 99 and o[:,1] <= 100:
            print("Success! Velocity = " + str(v) + " Angle = " + str(theta) + " Timestep = 0.0001 Time = " + str(o[:,0]) +" Current Runtime = " + str(round((time.time() - start_time), 2)))
            xResults.append(v)
            aResults.append(theta)
            tResults.append(float(o[:,0]))
            break
print("\n Total Runtime: " + str(time.time() - start_time))