import math
from math import pi

def circle_area(rad):
    # Check for valid input
    if type(rad) not in [int, float]:
        raise ValueError("Radius must be a number.")
    if rad < 0:
        raise ValueError("Radius cannot be negative.")
    return pi * (rad ** 2)

# Test function
radii = [2, 0, -3, 2 + 5j, True, "rad"]
message = "Area of circles with r = {rad} is {area}."

for r in radii:
    try:
        A = circle_area(r)
        print(message.format(rad=r, area=A))
    except ValueError as e:
        print(f"Error for r = {r}: {e}")


