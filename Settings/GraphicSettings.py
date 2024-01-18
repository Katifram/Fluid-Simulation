from dataclasses import dataclass


# Constants
@dataclass
class Screensettings:
    PARTICLE_COLOR: tuple = (0, 0, 255)
    BACKGROUND_COLOR: tuple = (255, 255, 255)
    WIDTH: int = 800
    HEIGHT: int = 600