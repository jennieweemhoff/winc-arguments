# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Greet Template
def greet(name, greeting='Hello, <name>!'): 
    return(greeting.replace('<name>', name))

# Force 
def force(mass, body='earth'):
    gravity = {
        'sun': 274, 
        'jupiter': 24.9,
        'neptune': 11.2, 
        'saturn': 10.4, 
        'earth': 9.8, 
        'uranus': 8.9, 
        'venus': 8.9,
        'mars': 3.7, 
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }

    if body in gravity: # check if gravity of body is provided in function
        force = mass * gravity[body] # calculate force 
        return force
    else:               # if gravity is not provided, return False
        return False 

# Gravity 
def pull(m1, m2, d): # mass in kg, distance in meters
    G = 6.674 * 10**-11 # gravitational constant
    F = G * ((m1 * m2) / d **2 ) 
    return F



