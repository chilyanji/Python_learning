# Create a function that return both the area and circumference of a circle given its radius.
import math

def circle(radius):
    print("The area of the given Circle is: ", ((math.pi*(radius**2))))
    print("Circumference of the given circle is: ", (2*math.pi*radius))

number = float(input("Enter the radius of a given circle: "))
circle(number)