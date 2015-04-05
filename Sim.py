# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis

# The simulation object
# This holds temporal (e.g. time related) data and is used to run the simulation
class Simulation():
    def __init__(self, delta_t, objects):
        self.dt = delta_t
        self.objs = objects
        self.cycles = 0

    def run(self, run_for):
        while run_for > 0:
            self.step()
            run_for -= 1 

    def __str__(self):
        return "Cycles run: %d\n" % (self.cycles)

    def step(self):
        for obj in self.objs:
            obj.update(self.dt)
        self.cycles += 1
        print self

        
