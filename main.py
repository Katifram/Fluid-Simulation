import pygame
import sys
from time import perf_counter
# import numpy as np

from physics import *
from graphics import *



print("hallo")

def main() -> None:

    # Timestep for first frame
    time_step: float = 0.1

    # Initialize
    screen = initialize_screen()
    particle_array: Particle = spawn_particles_random(Physicssettings.nrOfParticles, Physicssettings.particleSize)

    # Main loop
    while True:
        # at start and finish for frame timing
        start_time = perf_counter()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # apply forces
        apply_gravity(particle_array, time_step)

        #
        update_particles(particle_array, time_step)

        for i in range(len(particle_array)):
            particle_array[i].collision_check(Physicssettings.dampingFactor)

        draw_particles(particle_array, screen)

        # at start and finish for frame timing
        end_time = perf_counter()
        time_step = end_time - start_time
        print(time_step)


if __name__ == "__main__":
    main()

