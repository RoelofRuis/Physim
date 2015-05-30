# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis

from Obj import Motor
from collections import deque

# 1. Genereer een set auto's met willekeurige eigenschappen
# 2. Run de simulatie
# 3. Vind de auto's met de beste resultaten
# 4. Muteer deze auto's en ga naar 2, Herhaal voor x

class Evolver():
    def __init__(self, epochs, objects_simulator):
        self.obj_count = 100
        self.max_selected = 5
        self.epochs = epochs
        self.objects_simulator = objects_simulator
        self.current_run = self.init_random()
        self.current_results = []

    def evolve(self):
        n = 0
        print "ik evolve!"
        while n < self.epochs:
            print "Epoch %d now running..." % (n)
            n += 1
            self.run_epoch()
            best_selection = self.find_best()
            for t in list(best_selection):
                print t
            self.mutate(best_selection)

    def init_random(self):
        motors = []
        for o in range(self.obj_count):
            motors.append(self.generate_random_motor())
        return motors

    def generate_random_motor(self):
        return Motor.get_random()

    def run_epoch(self):
        self.current_results = self.objects_simulator.run_batch(self.current_run)

    def find_best(self):
        selected = deque([])
        best_val = 0
        for (motor, dist) in self.current_results:
            if dist >= best_val:
                best_val = dist
                if (len(selected) == self.max_selected):
                    selected.pop()
                selected.appendleft((motor, dist))
        return selected

    def mutate(self, best_selection):
        new_gen = []
        for (motor, dist) in best_selection:
            for n in range(20):
                new_gen.append(self.mutate_single(motor))
        self.current_run = new_gen

    def mutate_single(self, motor_obj):
        return motor_obj.mutate()
