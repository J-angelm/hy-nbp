import numpy as np
from nbp.NBPSolver import Body, NBPSolver

if __name__ == "__main__":
    sun     = Body(1.988E30, np.array([0, 0, 0]).astype(float), 
                np.array([0, 0, 0]).astype(float), "sun")
    mercury = Body(3.285E23, np.array([0, 5.7E10, 0]).astype(float),
                np.array([47000, 0, 0]).astype(float), "mercury")
    venus   = Body(4.8E24, np.array([0, 1.1E11, 0]).astype(float),
                np.array([35000, 0, 0]).astype(float), "venus")
    earth   = Body(5.9722E24, np.array([0, 1.5E11, 0]).astype(float), 
                np.array([30000, 0, 0]).astype(float), "earth")
    mars    = Body(2.4E24, np.array([0, 2.2E11, 0]).astype(float),
                np.array([24000, 0, 0]).astype(float), "mars")
    jupiter = Body(1E28, np.array([0, 7.7E11, 0]).astype(float),
                np.array([13000, 0, 0]).astype(float), "jupiter")
    saturn  = Body(5.7E26, np.array([0, 1.4E12, 0]).astype(float),
                np.array([9000, 0, 0]).astype(float), "saturn")
    uranus  = Body(8.7E25, np.array([0, 2.8E12, 0]).astype(float),
                np.array([6835, 0, 0]).astype(float), "uranus")
    neptune = Body(1E26, np.array([0, 4.5E12, 0]).astype(float),
                np.array([5477, 0, 0]).astype(float), "neptune")
    pluto   = Body(1.3E22, np.array([0, 3.7E12, 0]).astype(float),
                np.array([4748, 0, 0]).astype(float), "pluto")
    moon = Body(7.3476E22, np.array([0, 1.50383E11, 3.449E7]).astype(float), 
                np.array([31020.62, 0, -91.81]).astype(float), "moon")
    body_list = [sun, mercury, venus, earth, mars, jupiter, saturn, 
                    uranus, neptune, pluto, moon]
    ts = 10000
    nbp_solver = NBPSolver(body_list, ts)

    time_lim = 3.1536E7*21
    frame_size = 86400
    nbp_solver.plot_animation(time_lim, frame_size, "solar_sys.gif")