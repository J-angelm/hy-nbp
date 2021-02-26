# N Body Problem
#### *A quick implementation of the N Body Problem of Celestial Mechanics*

### Features
- Create *Bodies* with 3 initial parameters:
  param  |  dtype  |  description
  ------ | --------- | ---------
  *mass* | **float** | mass of the body
  *pos* | **np.array** | position vector <i, j, k> 
  *vel*    | **np.array** | scape velocity vector <i, j, k>
  
- Create an *NBPSolver* with two parameters:
  param  |  dtype  |  description
  ------ | --------- | ---------
  *bodies* | **list** | list of bodies
  *ts*     | **float**       | time step 

- Plot trajectories animation
    
- Utilize the NBPSolver method **_solve_timestep_** to update each body's position after the specified time step has passed.

- This package offers flexibility in terms of handling the output, as well as dinamically adding or removing bodies during run time.

### TODO:
  - Add different integration methods
  - Add efficiency monitoring (*hint: create a context manager to monitor execution times)
