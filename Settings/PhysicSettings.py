from dataclasses import dataclass

@dataclass
class Physicssettings:
    particleSize: float = 1.0
    nrOfParticles: int = 100
    particleSpacing: float = 50.0
    dampingFactor: float = 0.68
    particleInteraction: int = 100000
    forceOfGravity: float = 5
    sphereOfInfluence: float = 100.01  # times the radius
    mass: float = 1
