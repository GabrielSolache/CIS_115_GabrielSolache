#function to calculate energy using E=mc^2
def calculate_energy(mass):
    #speed of light in m/s
    c = 2.99 * (10**8)
    energy = mass * (c**2)
    return energy