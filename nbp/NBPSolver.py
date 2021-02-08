"""
NBPSolver (version 0.0.2)

author: J. Angel
date: 01/31/2020
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

"""
Each Body instance represents a single celestial object that is subject to
gravitational force from other objects and has 5 attributes at all times:
    mass            (float)
    pos             (np.array.astype(float))
    vel             (np.array.astype(float))
    accel           (np.array.astype(float))
    name            (string)
the acceleration is automatically initiated, all other values must be provided
at creation.
"""
class Body:
    def __init__(self, mass, pos, vel, name):
        self.mass = mass
        self.pos  = pos
        self.vel  = vel
        self.name = name
        self.accel = np.array([0, 0, 0]).astype(float)

    def __str__(self):
        return (self.name)

"""
The NBPSolver class provides the "environment" for bodies to interact (under 
gravitational force) by looping through a list of bodies and updating them by
a time step of size ts.
    bodies                      (list[Body, ...])
    ts                          (float)

    add_body(body):             add a Body object to list
    solve_timestep():           updates each body's pos, vel, and accel, by an  
                                increment of size "ts"
    plot_animation(time_lim,    generate a .gif plot animation of the bodies 
                   frame_size): trajectories
"""
class NBPSolver:
    def __init__(self, bodies, ts):
        self.bodies = bodies            # body list
        self.ts = ts                    # timestep

    def add_body(self, body):
        self.bodies.append(body)

    # update bodies position, velocity, and acceleration, 
    # according to Newton's law of gravity and the provided ts
    def solve_timestep(self):
        for body in self.bodies:
            body.accel = np.array([0, 0, 0]).astype(float)
            for xbody in [xbody for xbody in self.bodies if xbody != body]:
                # update acceleration
                body.accel += calc_a(body, xbody)
            # update velocity
            body.vel  += body.accel*ts
            # update position
            body.pos  += body.vel*ts
    # plot trajectories of lenght time_lim with frames of frame_size
    def plot_animation(self, time_lim, frame_size):
        # calc trajectories and store results
        traj_story = np.asarray([[body.pos] for body in self.bodies])
        time_spnt = 0
        while(time_spnt <= time_lim):
            self.solve_timestep()
            if (int(time_spnt) % frame_size == 0):
                traj_story = np.append(traj_story, 
                                    [[body.pos] for body in self.bodies], 
                                    axis=1)
            time_spnt += self.ts

        # draw main plot axes, set limits, scale
        fig = plt.figure(figsize=(8,5.5))
        ax = fig.gca(projection='3d', title="N Body Problem")
        colors = plt.cm.jet(np.linspace(0, 1, len(self.bodies)))
        plots = sum([ax.plot([],[],[], '-o', c=c, label=body, ) 
                    for c, body in zip(colors, self.bodies)], [])
        ax.set_xlim(-max(traj_story[:,:,0].flatten()), max(traj_story[:,:,0].flatten()))
        ax.set_ylim(-max(traj_story[:,:,1].flatten()), max(traj_story[:,:,1].flatten()))
        ax.set_zlim(-max(traj_story[:,:,2].flatten()), max(traj_story[:,:,2].flatten()))
        ax.view_init(30, 0)
        ax.set_xscale("symlog")
        ax.set_yscale("symlog")
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_zticklabels([])
        
        # main looped animation function 
        def animate(frame):
            for plot, traj in zip(plots, traj_story):
                plot.set_xdata(traj[frame, 0])
                plot.set_ydata(traj[frame, 1])
                plot.set_3d_properties(traj[frame, 2])

            ax.view_init(31, 0.3*frame)    
            return plots
        
        anim = animation.FuncAnimation(fig, animate, frames=traj_story[0,:,0].size,  
                                    interval=30, blit=True)

        anim.save("nbp-out.gif", fps=30)

# Newton's gravitational law
def calc_a(body, xbody):
    g_const         = 6.67408E-11
    bdy_xbdy_vector = xbody.pos - body.pos
    abs_vector      = np.sqrt(bdy_xbdy_vector.dot(bdy_xbdy_vector))
    return ((g_const*xbody.mass)/np.power(abs_vector,2))*((1/abs_vector)*bdy_xbdy_vector)
    