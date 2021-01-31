import numpy as np

class NBPSolver:
    def __init__(self, bodies, ts):
        self.bodies = bodies
        self.ts = ts               # timestep
        
    gconst = 6.674E-11

    def add_body(self, body):
        self.bodies.append(body)

    def solve_timestep(self):
        for body in self.bodies:
            self.update_values(body, [xbody for xbody in self.bodies if xbody != body])

    def update_values(self, body, bodies):
        #update_accel(body, bodies)
        for xbody in bodies:
            new_accel = self.calc_a(body, xbody)
        body.accel = new_accel
        #update_speed(body, bodies)
        body.vel += body.accel*self.ts
        #update_position(body, bodies)
        body.pos += body.accel*self.ts

    def calc_a(self, body, xbody):
        rvector = body.pos - xbody.pos
        abs_vector = np.sqrt(rvector.dot(rvector))
        return ((self.gconst*xbody.mass)/abs_vector)*((1/abs_vector)*rvector)

class Body:
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos  = pos
        self.vel  = vel
    accel = np.array([0, 0, 0])

if __name__ == "__main__":
    earth_mass = 5.972E24
    earth_pos  = np.array([0, 1.5E11, 0]).astype(float)
    earth_vel  = np.array([-3E4, 0, 0]).astype(float)
    earth = Body(earth_mass, earth_pos, earth_vel)

    moon_mass = 7.3476E22
    moon_pos  = np.array([0, 1.50383E11, 3.449E7]).astype(float)
    moon_vel  = np.array([-31020.62, 0, -91.81]).astype(float)
    moon = Body(moon_mass, moon_pos, moon_vel)

    sun_mass = 1.988E30
    sun_pos  = np.array([0, 0, 0]).astype(float)
    sun_vel  = np.array([0, 0, 0]).astype(float)
    sun = Body(sun_mass, sun_pos, sun_vel)

    body_list = [earth, moon, sun]

    ts = 0.1
    nbp_solver = NBPSolver(body_list, ts)

    time_lim  = 10
    time_spnt = 0
    while (time_spnt < time_lim):
        nbp_solver.solve_timestep()
        for idx, body in enumerate(nbp_solver.bodies): 
            print(idx, body.pos)
        time_spnt += ts