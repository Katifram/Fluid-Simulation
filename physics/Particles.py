import random
import numpy as np
# import math

from Settings import Screensettings
from . import Physicssettings
# from utils import calculate_angle
# from utils import PosNeg


from decorator_func import benchmark

random.seed()


class Particle:

    def __init__(self, size: float, position: list[float], velocity: list[float], acceleration: list[float]):
        self.size = size
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def apply_force(self, force: list[float]):
        delta_acceleration = [element / Physicssettings.mass for element in force]
        self.acceleration += [a + b for a, b in zip(self.acceleration, delta_acceleration)]

    def collision_check(self, dampingfactor: float):
        # check colissions with floor and ceiling
        if self.position[0]-self.size < 0:
            self.position[0] = self.size
            self.velocity[0] *= -1*dampingfactor
        if self.position[0]+self.size > Screensettings.HEIGHT:
            self.position[0] = Screensettings.HEIGHT-self.size
            self.velocity[0] *= -1*dampingfactor
        # check colissions with left and right wall
        if self.position[1]-self.size < 0:
            self.position[1] = self.size
            self.velocity[1] *= -1*dampingfactor
        if self.position[1]+self.size > Screensettings.HEIGHT:
            self.position[1] = Screensettings.HEIGHT-self.size
            self.velocity[1] *= -1*dampingfactor


def spawn_particles_grid(num_particles: int, size: float):
    nr_particles_row = int(np.sqrt(num_particles))
    particle_array = []
    for i in range(num_particles):
        # Create a Particle object and add it to the array
        x = i % nr_particles_row * size * 2 + Physicssettings.particleSpacing
        y = int(i / nr_particles_row) * size * 2 + Physicssettings.particleSpacing
        particle = Particle(size=size, position=[x, y], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
        particle_array.append(particle)
    return particle_array


def apply_gravity(particle_array: list[Particle], time_step: float):
    for Particles in particle_array:
        Particles.acceleration[1] += 9.81 * Physicssettings.forceOfGravity * time_step  # 9.81 because it's real
    return


def update_particles(particle_array: list[Particle], time_step: float):
    for Particles in particle_array:
        Particles.velocity = [a + b for a, b in zip(Particles.velocity, Particles.acceleration)]
        delta_position = [element * time_step for element in Particles.velocity]
        Particles.position = [a + b for a, b in zip(Particles.position, delta_position)]


def spawn_particles_random(num_particles: int, size: float):
    particle_array = []
    for i in range(num_particles):
        # Create a Particle object and add it to the array
        x = random.uniform(0, Screensettings.WIDTH)
        y = random.uniform(0, Screensettings.HEIGHT)
        particle = Particle(size=size, position=[x, y], velocity=[0.0, 0.0], acceleration=[0.0, 0.0])
        particle_array.append(particle)
    return particle_array


def smooth_particle(radius: float, distance: float):
    volume = np.pi * radius**8 / 4
    value = max(0.0, radius**2 - distance**2)
    return value**3 / volume



# def calculate_density(point: list(float), particle_array):
#     density = 0
#     mass = 1
#     particle_array


# checks 2 Particles and gives the interaction force for the first one
# @benchmark
# def particle_interaction(particle_array: list[Particle]):
#     for i in range(len(particle_array)):
#         for j in range(i + 1, len(particle_array)):
#             # calculate distance
#             angle = calculate_angle(particle1.position, particle2.position)
#             distance = math.dist(particle1.position, particle2.position)
#             # calculate force
#             totalforce: float = Physicssettings.particleInteraction * smooth_particle(Physicssettings.particleSize*Physicssettings.sphereOfInfluence, distance)
#             force = np.zeros(2, float)
#             # particle in x
#             force[0] = totalforce * np.cos(angle)
#             # particle in y
#             force[1] = totalforce * np.sin(angle)
#             return force
