# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis

from Obj import MassiveObject, Spring

# The simulation object
# This holds temporal (e.g. time related) data and is used to run the simulation
class Simulation():
    def __init__(self, delta_t, objects, prnt = False):
        self.dt = delta_t
        self.objs = objects
        self.cycles = 0
        self.prnt = prnt

    def get_prnt(self):
        return self.prnt

    def run(self, run_for):
        while run_for > 0:
            self.step()
            run_for -= 1 

    def __str__(self):
        return "Cycles run: %d\n" % (self.cycles)

    def step(self):
        for obj in self.objs:
            obj.update(self.dt)
            if self.prnt:
                print obj
        self.cycles += 1
        if self.prnt:
            print self

    def results(self, prnt = False):
        results = []
        for obj in self.objs:
            results.append(obj.getDistance())
            if prnt:
                print obj 
        if prnt:
            print self
        return results

class Objects():
    def __init__(self, delta_t, carproperties):
        self.steps = 1000
        self.delta_t = delta_t
        self.car_prop = carproperties
        self.objects = []

    def run_batch(self, motordrive):
        results = []
        for m in motordrive:
            spring =  Spring(
                self.car_prop["spring_const"],
                self.car_prop["init_spring_ext"],
                self.car_prop["arm_length"],
                self.car_prop["wheel_big"],
                self.car_prop["wheel_small"],
                self.car_prop["min_ext"])
            sim = Simulation(self.delta_t, [MassiveObject(self.car_prop["mass"],
                                              self.car_prop["area"],
                                              self.car_prop["drag_coeff"],
                                              self.car_prop["roll_res_coeff"],
                                              spring
                                              )])
            sim.run(self.steps)
            res = sim.results()
            results.append((m, res[0]))
        return results
            
        
