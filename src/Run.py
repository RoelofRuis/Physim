# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis
from Obj import Spring, MassiveObject
from Sim import Objects, Simulation
from Search import Evolver
import random
from operator import add, sub, mul, div
import math
import random

delta_t = 1

epochs = 100

car_properties = {"mass" : 0.7,
                  "area" : 0.2,
                  "drag_coeff" : 0.15,
                  "roll_res_coeff" : 0.03,
                  "spring_const" : 0.05,
                  "init_spring_ext" : 293,
                  "arm_length": 31,
                  "wheel_big" : 13,
                  "wheel_small" : 3,
                  "min_ext" : 228}

e = Evolver(epochs, Objects(delta_t, car_properties))

e.evolve()

'''
delta_t = 1

# Object properties

mass = 0.6
area = 0.2
drag_coeff = 0.15
roll_res_coeff = 0.03
spring_const = 0.05
init_spring_ext = 345
arm_length = 31
wheel_big = 13
wheel_small = 3
min_ext = 288


# Initiate the spring
spring = Spring( spring_const, init_spring_ext, arm_length, wheel_big, wheel_small, min_ext)

# Initiate the objects participating in the simulation
objects = [
    MassiveObject(mass, area, drag_coeff, roll_res_coeff, spring, [6, 27, 2, add, math.sqrt])
    ]



s = Simulation(delta_t, objects, prnt = True)

# Run the simulation
s.run(100)
'''

