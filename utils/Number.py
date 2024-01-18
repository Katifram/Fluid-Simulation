import math

# returns 1 for positive and -1 for negative "number"
def pos_neg(number):
    if number >= 0:
        return 1
    else:
        return -1


def calculate_angle(point1, point2):
    # point1 and point2 should be tuples or lists representing (x, y) coordinates
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences in x and y coordinates
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Calculate the angle in radians using arctangent
    angle_rad = math.atan2(delta_y, delta_x)

    # Convert the angle to degrees
    angle_deg = math.degrees(angle_rad)

    return angle_deg