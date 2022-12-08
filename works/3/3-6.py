def pressure(v,t,n = 6.022e23):
    '''Compute the pressure in pascals of an ideal gas
    
    v --- volume of gas, in cubic meters
    t --- absolute temperature in degrees Kelvin
    n --- particals of gas (default: one mole)
    '''
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v