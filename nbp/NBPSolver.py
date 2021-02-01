from numpy import array, sqrt

class Body:
    def __init__(self, mass, pos, vel, 
                accel = array([0, 0, 0]).astype(float)):
        self.mass = mass
        self.pos  = pos
        self.vel  = vel
        self.accel = accel

class NBPSolver:
    def __init__(self, bodies, ts):
        self.bodies = bodies
        self.ts = ts               # timestep

    def add_body(self, body):
        self.bodies.append(body)

    def solve_timestep(self):
        for body in self.bodies:
            update_values(body, 
            [xbody for xbody in self.bodies if xbody != body], self.ts)

def update_values(body, bodies, ts):
    #update acceleration
    for xbody in bodies:
        new_accel  = array([0, 0, 0]).astype(float)
        new_accel += calc_f(body, xbody)
    body.accel = new_accel
    #update speed
    body.vel  += body.accel*ts
    #update position
    body.pos  += body.accel*ts

def calc_f(body, xbody):
    gconst          = 6.674E-11
    bdy_xbdy_vector = body.pos - xbody.pos
    abs_vector      = sqrt(bdy_xbdy_vector.dot(bdy_xbdy_vector))
    return ((gconst*xbody.mass)/abs_vector)*((1/abs_vector)*bdy_xbdy_vector)

if __name__ == "__main__":
    earth_mass = 5.972E24
    earth_pos  = array([0, 1.5E11, 0]).astype(float)
    earth_vel  = array([-3E4, 0, 0]).astype(float)
    earth = Body(earth_mass, earth_pos, earth_vel)

    moon_mass = 7.3476E22
    moon_pos  = array([0, 1.50383E11, 3.449E7]).astype(float)
    moon_vel  = array([-31020.62, 0, -91.81]).astype(float)
    moon = Body(moon_mass, moon_pos, moon_vel)

    sun_mass = 1.988E30
    sun_pos  = array([0, 0, 0]).astype(float)
    sun_vel  = array([0, 0, 0]).astype(float)
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