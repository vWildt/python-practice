import math

def area_circle(radius):
    """Return area of a circle with the given radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    area = area_circle(r)
    print(f"The area is {area}")
