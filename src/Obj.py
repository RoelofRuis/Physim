# Mousetrap car simulation
#
# By Felix Brakel & Roelof Ruis
#
# This file contains the objects used in the simulation

from __future__ import division
import math
#from Run import springs

# An object with mass
class MassiveObject():
    def __init__(self, mass, area, drag_coeff, roll_res_coeff, spring):
        self.m = mass
        self.Cd = drag_coeff
        self.Crr = roll_res_coeff
        self.s = 0
        self.v = 0
        self.a = 0
        self.F = 0
        self.A = area
        self.spring = spring
        spring.attach(self)
    
    def __str__(self):
        return ("MassiveObject\n\t"
                    "Mass: %.2f\n\t"
                    "Drag Coefficient: %.2f\n\t"
                    "Roll Resistance Coefficient: %.2f\n\t"
                    "Cross Sectional Area: %.2f\n\t"
                    "Acceleration: %.2f\n\t"
                    "Velocity: %.2f\n\t"
                    "Force:\n\t\t"
                    "Motor Force: %.2f\n\t\t"
                    "Spring Force %.2f\n\t\t"
                    "Drag: %.2f\n\t\t"
                    "Roll Resistance: %.2f\n\t"
                    "Distance: %.2f") % (self.m, self.Cd, self.Crr, self.A, self.a, self.v, self.f_motor, self.f_spring, self.f_drag, self.f_roll, self.s)

    def getMass(self):
        return self.m

    def getDragCoefficient(self):
        return self.Cd

    def getRollResistanceCoefficient(self):
        return self.Crr
    
    def getDistance(self):
        return self.s

    def getVelocity(self):
        return self.v

    def update(self, delta_t):
        self.updateForces(delta_t)
        self.updateDistance(delta_t)
        print self

    def updateForces(self, delta_t):
        density = 1.29
        gravity = 9.81
        
        self.f_motor = 0
        self.f_spring = self.spring.unwind(delta_t)
        self.f_drag = 0.5 * density * pow(self.v, 2) * self.Cd * self.A
        self.f_roll = self.Crr * (self.m * gravity)

        f_drive = max((self.f_spring + self.f_motor) - self.f_roll, 0)
        f_counter = self.f_drag

        self.F = f_drive - f_counter if f_drive >= 0 else f_drive + f_counter

    def updateDistance(self, delta_t):
        self.a = self.F / self.m
        self.v += self.a * delta_t
        self.s += self.v * delta_t


# Functioning of the spring object is far from optimal.
# Possible improvements include:
# - update extension based on amount of force supplied
# - base force supplied on the distance the wheel roled during this step
class Spring():
    def __init__(self, spring_constant, init_ext, arm_length, wheel_radius_big, wheel_radius_small):
        self.c = spring_constant
        self.init_u = init_ext
        self.A = arm_length
        self.u = self.init_u
        self.strng = 0
        self.whl_bg = wheel_radius_big
        self.whl_sml = wheel_radius_small
        self.circmfer_whl_bg = 2 * math.pi * self.whl_bg
        self.circmfer_whl_sml = 2 * math.pi * self.whl_sml

    def attach(self, obj):
        self.parent = obj

    def unwind(self, delta_t):
        force = ((self.c * self.u) / self.A) * (self.whl_sml / self.whl_bg)
        if force > 0:
            self.updateExtension()
            self.updateString(delta_t)
            return force
        else:
            return 0

    def updateExtension(self):
        self.u = 360 - math.degrees( math.acos( (pow(self.strng, 2) - (2 * pow(self.A, 2))) / (-2 * (self.A * self.A)) ))

    def updateString(self, delta_t):
        v = self.parent.getVelocity()
        delta_s = v * delta_t
        revolutions = delta_s / self.circmfer_whl_bg
        self.strng += revolutions * self.circmfer_whl_sml
        
        
        
        
        
