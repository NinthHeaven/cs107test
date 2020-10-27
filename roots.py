#!/usr/bin/env python3
import cmath

# Functions based off lecture12
def quad_roots(a=1.0, b=1.0, c=1.0):
    # Documentation taken directly from lecture 12
    """Returns the roots of a quadratic equation: ax^2 + bx + c = 0.

    INPUTS
    =======
    a: float, optional, default value is 1
       Coefficient of quadratic term
    b: float, optional, default value is 2
       Coefficient of linear term
    c: float, optional, default value is 0
       Constant term

    RETURNS
    ========
    roots: 2-tuple of complex floats
       Has the form (root1, root2) unless a = 0 
       in which case a ValueError exception is raised
    
    EXAMPLES
    =========
    >>> quad_roots(1.0, 1.0, -12.0)
    ((3+0j), (-4+0j))
    """
    if a == 0:
        raise ValueError("You entered an a value that equals to 0. This is not a quadratic equation.")
    
    # Create sqrt(b^2 - 4ac)
    sq_root = cmath.sqrt(b**2.0 - 4.0*a*c)

    # Create nominators to apply +/- scenarios
    upper1 = -b + sq_root
    upper2 = -b - sq_root

    # Create denominator
    lower = 2.0*a

    # Return root equation
    return (upper1/lower, upper2/lower)

def linear_roots(a=1.0, b=1.0):
    # Documentation taken directly from lecture12
    """Returns the roots of a linear equation: ax+ b = 0.
    
    INPUTS
    =======
    a: float, optional, default value is 1
       Coefficient of linear term
    b: float, optional, default value is 0
       Coefficient of constant term
    
    RETURNS
    ========
    roots: 1-tuple of real floats
       Has the form (root) unless a = 0 
       in which case a ValueError exception is raised
    
    EXAMPLES
    =========
    >>> linear_roots(1.0, 2.0)
    -2.0
    """
    if a == 0:
        raise ValueError("You entered an a value that equals to 0. This is not a linear equation.")

    # Return roots of linear function
    return (-b/a)
