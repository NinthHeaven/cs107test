import cmath

def quad_roots(a=1.0, b=1.0, c=1.0):
    #TODO Enter Doc up here
    if a == 0:
        raise ValueError("You entered an a value that equals to 0. This is not a quadratic equation.")
    
    # Create sqrt(b^2 - 4ac)
    sq_root = cmath.sqrt(b**2 - 4*a*c)

    # Create nominators to apply +/- scenarios
    upper1 = -b + sq_root
    upper2 = -b - sq_root

    # Create denominator
    lower = 2*a

    # Return root equation
    return (upper1/lower, upper2/lower)

def linear_roots(a=1.0, b=1.0):
    #TODO Enter Doc up here
    if a == 0:
        raise ValueError("You entered an a value that equals to 0. This is not a linear equation.")

    # Return roots of linear function
    return -b/a