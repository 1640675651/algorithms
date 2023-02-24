from math import pi
from math import sqrt
from math import atan
def cartesian2polar(x, y):
    r = sqrt(x**2+y**2)
    if x != 0: # avoid division of zero
        alpha = atan(y/x)
        if x<0: # atan only returns angle from -90 to 90. need to manually adjust.
            alpha += pi
        elif x>0 and y<0:
            alpha += 2*pi
    else:
        if y>=0:
            alpha = pi/2
        elif y<0:
            alpha = 3*pi/2

    return r, alpha
