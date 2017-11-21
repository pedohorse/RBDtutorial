This is supplementary material for the RBD try-to-be-tutorial for Houdini that can be found here:

## Part 1

* ### example_com
This example shows you how center of mass is calculated
You can see how any object is divided into tetrahedrons, orange arrows will be pointint to those tetrahedrons' centers of masses.
Red arrow is pointint to the whole object's center of mass

Use the display node to change the visualisation scale of tetrahedrons to understand better how they fill up the mesh

You can plug your custom object into *"PUT_OBJECT_HERE"* red null.
Just remember, that for calculations to be correct the object has to be closed, with little-to-none self intersections

* ### example_mom_of_inert
This example shows how moment of inertia is calculated
You may see the object and it's calculated rest(I0) and current(I) moment of inertia matrices

Use the display node to change object's rotation and see how I changes with it

You can plug your custom object into *PUT_ANY_RAW_OBJECT_HERE* red null.
as in com example, remember to keep the object closed and without self intersections (we are working with physically correct objects here after all)

* ### example_rotate_in_a_proper_way
This example shows different ways RBD integrator can work, and compares it with Houdini's standard Bullet's integrator.

Use the display node to change solver type
  0. Trivial integrator, one that keeps angular velocity(w) constant, witch is the most fast and simple way to implement integrator, but which leads to non physically correct behaviour, including possible energy additions and subtractions
  1. Simplest physically correct integrator, uses Euler first order integration method - not accurate, requires high substeps to converge
  2. Same simplest physically correct integrator, but using second order Euler-trapezoid predictor-corrector method - notice how much more accurate it becomes with significantly less substeps
  3. Bullet integrator. Notice that bullet does integration pretty neat, though at high velocities does not converge properly, and tend to reduce energy during calculations - probably it helps keeping big simulations more stable.
 
## How to launch
* use the python launcher script provided, it's supposed to cover both windows and linux/mac cases
* use chLauncher to launch - there is a preconfigured project supplied
* or just manually set following env variables if you are using your ways of starting houdini
	* HOUDINI_OTLSCAN_PATH = "<project's root>/otls:&"
	* HOUDINI_VEX_PATH = "<project's root>/vex:&"
