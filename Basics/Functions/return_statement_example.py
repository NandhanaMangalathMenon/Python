#Return Statement


import math  # Import math for pi

def compute_area(radius):
    #This defines a new function named compute_area that takes one value, radius, as its input
    # Calculate area using formula pi * r^2
    area = math.pi * radius * radius
    return area  # Return the computed area
#This returns the value of area from the function back to wherever the function was called.
#The return statement gives you access to the calculated value outside the function.

# Accept radius from the user and convert to float
radius = float(input("Enter the radius of the circle: "))

# Call the function to compute area
circle_area = compute_area(radius)
#This line calls the compute_area function, passing the radius value from the user as the argument.

# Display the result
print("Area of the circle is:", circle_area)
