# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis
from Sim import Objects
from Search import Evolver

delta_t = 1
epochs = 10

car_properties = {"mass" : 600,
                  "area" : 0.02,
                  "drag_coeff" : 0.15,
                  "roll_res_coeff" : 10,
                  "spring_const" : 20,
                  "init_spring_ext" : 293,
                  "arm_length": 31,
                  "wheel_big" : 13,
                  "wheel_small" : 3,
                  "min_ext" : 228}

e = Evolver(epochs, Objects(delta_t, car_properties))

e.evolve()
