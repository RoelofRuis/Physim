# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis

from Obj import MassiveObject, Spring
from Sim import Simulation

# Timescale of the simulation
delta_t = 1

# Object properties
mass = 200
area = 0.01
drag_coeff = 0.01
roll_res_coeff = 0.01
spring_const = 2
init_spring_ext = 345
arm_length = 20
wheel_big = 10
wheel_small = 2

# Initiate the spring
springs = [
    Spring( spring_const, init_spring_ext, arm_length, wheel_big, wheel_small)
    ]

# Initiate the objects participating in the simulation
objects = [
    MassiveObject(mass, area, drag_coeff, roll_res_coeff, springs[1])
    ]


# Initiate the simulation object
s = Simulation(delta_t, objects)

# Run the simulation
s.run(100)
