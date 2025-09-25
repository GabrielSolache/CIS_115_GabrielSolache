#function to calculate the angle theta of a right tringle 
def calculate_theta(x, y):
    #Calculates angle using atan2 and converts radian to degrees
    theta_radians = math.atan2(y, x)
    theta_degree = theta_radians * (180 / math.pi)
    print(f"The angle theta is:{theta_degree:.2f} degrees")
