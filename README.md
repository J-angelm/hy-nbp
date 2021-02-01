# N Body Problem API
#### *An easy implementation of the N Body Problem of Celestial Mechanics*

### Features
- Create *Bodies* with 3 initial parameters:
  - mass                     type: **float**
  - position vector          type: **np.array**
  - init. velocity vector    type: **np.array**
  
- Create an *NBPSolver* with two parameters:
  - list of bodies      type: **list**
  - time step           type: **float**
    
Utilize the NBPSolver method *solve_timestep* to update the bodies position after a the specified time step has spent.

This package offers flexibility in terms of the desired output, since it works by updating its list of bodies on each time step iteration. This also allows for flexibility in terms of the number of bodies desired at any given instant (list of bodies can be modified on the run).

### TODO:
  - Add different integration methods
  - Add test cases
