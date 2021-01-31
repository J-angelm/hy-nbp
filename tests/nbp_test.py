import numpy as np
from nbp.NBPSolver import NBPSolver, Body

earth_mass = 5.972E24
earth_pos  = np.array([0, 1.5E11, 0])
earth_vel  = np.array([-3E4, 0, 0])
earth = Body(earth_mass, earth_pos, earth_vel)

moon_mass = 7.3476E22
moon_pos  = np.array([0, 1.50383E11, 3.449E7])
moon_vel  = np.array([-31020.62, 0, -91.81])
moon = Body(moon_mass, moon_pos, moon_vel)

sun_mass = 1.988E30
sun_pos  = np.array([0, 0, 0])
sun_vel  = np.array([0, 0, 0])
sun = Body(sun_mass, sun_pos, sun_vel)

body_list = [earth, moon, sun]

ts = 0.1
nbp_solver = NBPSolver(body_list, ts)

time_lim  = 10
time_spnt = 0
while (time_spnt < time_lim):
    nbp_solver.solve_timestep()
    for body in nbp_solver.bodies:
        print(body.pos)
    time_spnt += ts

    



