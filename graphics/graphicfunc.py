from dataclasses import dataclass
from physics import Particle
from physics import Physicssettings
from Settings import Screensettings
import pygame


def initialize_screen():
    pygame.init()
    # Create a screen
    screen = pygame.display.set_mode((Screensettings.WIDTH, Screensettings.HEIGHT))
    pygame.display.set_caption("Water Physics Engine")
    return screen


def draw_particles(particle_array: list[Particle], screen):
    # Draw particles on the screen
    screen.fill(Screensettings.BACKGROUND_COLOR)
    for Particles in particle_array:
        Particles.collision_check(Physicssettings.dampingFactor)
        pygame.draw.circle(screen, Screensettings.PARTICLE_COLOR,
                           (int(Particles.position[0]), int(Particles.position[1])),
                           int(Particles.size))
    pygame.display.flip()
